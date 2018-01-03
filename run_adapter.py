from adapter import ImageAdaptor

img_adapt = ImageAdaptor(
    litlang1_path="/media/lucas/18th C Collections Online/ECCO_2of2/LitAndLang_1",
    litlang2_path="/media/lucas/18th C Collections Online/ECCO_2of2/LitAndLang_2",
    input_data_path='sampledata.txt',
    tiff_output_path='/home/lucas/dev/tiffsout/')
img_adapt.create_images()
