import os
from XmlUtility import XmlUtility
import argparse
import xml.etree.ElementTree as xml
import Constants

class PipelineUtility:
    """Pipeline class"""

    @staticmethod
    def update_pipeline_corpus(pipeline_xml, corpus_url):
        try:
            reader_configuration_element = pipeline_xml.getroot().find("uima:collectionReader/uima:collectionIterator/uima:configurationParameterSettings", Constants.namespaces_pipeline)
            file_location_string_element = reader_configuration_element.find(
                "uima:nameValuePair[uima:name='INPUT_FILE']/uima:value/uima:string", Constants.namespaces_pipeline)
            if None == file_location_string_element:
                file_location_string_element = reader_configuration_element.find(
                    "uima:nameValuePair[uima:name='FILE_URL']/uima:value/uima:string", Constants.namespaces_pipeline)
            file_location_string_element.text = corpus_url
            use_relative_paths_nvp_element = reader_configuration_element.find(
                "uima:nameValuePair[uima:name='USE_RELATIVE_PATHS']", Constants.namespaces_pipeline)
            if use_relative_paths_nvp_element is None:
                PipelineUtility.add_use_relative_paths_equals_false(reader_configuration_element)
            else:
                use_relative_paths_boolean_element = use_relative_paths_nvp_element.find\
                    ("uima:value/uima:boolean", Constants.namespaces_pipeline)
                use_relative_paths_boolean_element.text = "false"
        except Exception as e:
            print("Exception in Update Pipeline Corpus Method, Error : ", e)

    @staticmethod
    def add_use_relative_paths_equals_false(reader_configuration_element):
        nvp = xml.Element("nameValuePair")
        reader_configuration_element.append(nvp)
        name_element = xml.Element("name")
        name_element.text = "USE_RELATIVE_PATHS"
        nvp.append(name_element)
        value_element = xml.Element("value")
        nvp.append(value_element)
        boolean_element = xml.Element("boolean")
        boolean_element.text = "false"
        value_element.append(boolean_element)

    @staticmethod
    def update_pipeline(pipeline_file_path, corpus_url):
        try:
            pipeline_xml = XmlUtility.parse_xmlns(pipeline_file_path)
            PipelineUtility.update_pipeline_corpus(pipeline_xml, corpus_url)
            XmlUtility.fixup_xmlns(pipeline_xml.getroot())
            pipeline_xml.write(pipeline_file_path)
        except IOError as e:
            print("Exception in Update Pipeline Method. Error : ", e)

if __name__ == "__main__":
    pipelineUtility = PipelineUtility()
