import os

import plac
from google_trans_new import google_translator


def main(input_file, output_file):
    assert os.path.exists(input_file), "Input file doesn't exist."

    translator = google_translator()

    with open(input_file, "rt", encoding='utf-8') as infile:
        with open(output_file, "w+", encoding='utf-8') as outfile:
            # First row in the input file
            header = infile.readline()

            # Write the same header in the output file
            outfile.write(header)

            # Read the first line to know the languages we're going to ask google to translate
            languages = [lang.strip() for lang in header.split(',')[1:]]

            print(f"Translating English to the following: {languages}")

            lines = infile.readlines()

            for line in lines:
                english_text = line.split(',')[0]

                translations = [translator.translate(english_text, lang_src='en', lang_tgt=lang) for lang in languages]

                print(f"en -> {english_text}")
                for language, translation in zip(languages, translations):
                    print(f"    {language} -> {translation}")

                outfile.write(english_text + ",")

                for translation in translations:
                    outfile.write(translation + ",")

                outfile.write('\n')


if __name__ == '__main__':
    plac.call(main)
