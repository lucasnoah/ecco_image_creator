import csv
#from storage.sql_alchemy_models import Line, set_up_db_session
from PIL import Image
import os
import codecs


class ImageAdaptor:
    def __init__(self,
                 litlang1_path: str,
                 litlang2_path: str,
                 input_data_path: str,
                 tiff_output_path: str):
        self.litlang1_path = litlang1_path
        self.litlang2_path = litlang2_path
        self.input_data_path = input_data_path
        self.tiff_output_path = tiff_output_path
        self.parsed_data = self.parse_input_data()

    def parse_input_data(self):
        """
        Parse the input data into python from the spreadsheet input.
        """
        lines_to_parse = []
        with codecs.open(
                self.input_data_path, "r", encoding='utf-8',
                errors='ignore') as f:
            lines = f.readlines()
            for line in lines:
                l = line.split("\t")
                coordinates = l[1][1:-1].split(",")
                line_dict = {
                    "line_uuid": l[0],
                    "coordinates": tuple(coordinates),
                    "ecco_doc_id": l[2],
                    "ecco_record_id": l[3],
                    "doc_quality_status": l[4],
                    "output_name": l[0] + '.tiff',
                    "original_text": None
                }

                if line_dict.get("doc_quality_status") == "good":
                    line_dict["original_text"] = l[5][1:-2]

                lines_to_parse.append(line_dict)

        return lines_to_parse

    def crop_image(self, coord_tuple, img, output_file_name):
        img = Image.open(img)
        img2 = img.crop(coord_tuple)
        img2.save(output_file_name)
        img2.close()
        return " "

    def get_image_path(self, image_name, record_name):
        lit_lang1_folder = self.litlang1_path
        lit_lang2_folder = self.litlang2_path
        file_name_1 = lit_lang1_folder + "/" + str(
            record_name) + "/images/" + image_name
        file_name_2 = lit_lang2_folder + "/" + str(
            record_name) + "/images/" + image_name
        print(file_name_1)
        print(file_name_2)
        if os.path.isfile(file_name_1):
            return file_name_1
        if os.path.isfile(file_name_2):
            return file_name_2
        else:
            return None

    def create_images(self):
        """
        Print tiff files from input_data
        """
        for line in self.parsed_data:
            image_path = self.get_image_path(
                line.get("ecco_record_id"), line.get("ecco_doc_id"))
            print("img_path", image_path)
            if image_path is not None:
                split_line = line.get("coordinates")
                image_location = (int(split_line[0]), int(split_line[1]),
                                  int(split_line[2]), int(split_line[3]))
                self.crop_image(
                    image_location, image_path,
                    self.tiff_output_path + line.get("line_uuid") + ".TIFF")
