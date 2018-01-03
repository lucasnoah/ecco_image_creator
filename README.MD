# ECCO FILE IMAGE ADAPTER

This projects serves as an adapter between flat files printed from our database and the .TIF images you will need for your OCR tasks.  


## installing dependencies
The project requires python3 and some basic dependencies.  You can install them
by running

`pip3 install -r requirements.txt`

## Creating the images

You can print the images by instantiating the ImageAdaptor class and calling the create_images fuction.  Below is an example.

`img_adapt = ImageAdaptor(
    litlang1_path="/media/lucas/18th C Collections Online/ECCO_2of2/LitAndLang_1",
    litlang2_path="/media/lucas/18th C Collections Online/ECCO_2of2/LitAndLang_2",
    input_data_path='test_data/goodbad.txt',
    tiff_output_path='/home/lucas/dev/tiffsout/')`

`img_adapt.create_images()`

You must supply the ImageAdaptor class with the folders for lit_and_lang_1 and lit_and_lang2 from your local copy of the ECCO database image set.  You must also, supply the input flat file location and the output folder where you would like to store the tiffs.

I have included a run_adapter.py file that you can modify and call yourself.
