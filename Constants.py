#!/usr/bin/python

legacy_directory_label = "Legacy_CPT"
constraint_path_directory_label = "Constraint_Path_CPT"
coderyte_svn = "https://svn.coderyte.net/coderyte/"
uima_trunk_url = coderyte_svn + "uima/trunk"
corpora_dir = "/home/jenkins/corpora"
uima = "uima"
engine = "engine"
uima_trunk = "uima_trunk"
nlpengine_dictionary = "nlpengine-dictionary"
nlpengine_parser = "nlpengine-parser"
nlpengine_constaint_engine = "nlpengine-constraint-engine"
trunk = "trunk"
code = "code"
desc = "desc"
pipelines = "pipelines"
events = "start", "start-ns"
start_ns = "start-ns"
xmlns = "xmlns:"
start = "start"
namespaces_pom = {'mvn': 'http://maven.apache.org/POM/4.0.0'}
pom = "pom.xml"
mvn = "mvn"
clean = "clean"
install = "install"
mvn_properties = "mvn:properties"
mvn_version = "mvn:version"
namespaces_pipeline = {'uima': 'http://uima.apache.org/resourceSpecifier'}

non_phi_files_to_copy = [
    "DiceCodeEvaluation.csv",
    "DiceClinicalIndicatorEvaluation.csv",
    "NonExistentFile.csv"
]

stats_configuration_files = [
    "I10CMCodeEvaluation.csv",
    "I10PCSCodeEvaluation.csv",
    "I10PCSCodeEvaluation.csv",
    "finalCodeEvaluation.08.code_selector.csv",
    "finalCodeEvaluation.09.code_selector.csv",
    "finalCodeEvaluation.17.code_selector.csv",
    "finalCodeEvaluation.Legacy.09.code_selector.csv",
    "finalCodeEvaluation.Legacy.17.code_selector.csv",
    "finalCodeEvaluation.CPT.09.code_selector.csv",
    "finalCodeEvaluation.CPT.17.code_selector.csv"
]

extra_files_to_copy = [
    "constraint_path_log.txt",
    "code_statistics",
    "DiceClinicalIndicatorEvaluation.csv",
    "DiceCodeEvaluation.csv",
    "DiceCodeBlockEvidence.csv",
    "primary_icd_evaluation.csv",
    "region",
    "evidence"
]

projects = [
"nlpengine-ctakes",
"nlpengine-common",
"nlpengine-preprocessing",
"nlpengine-measurements",
"nlpengine-dictionary",
"nlpengine-parser",
"nlpengine-doctype",
"nlpengine-wsd",
"nlpengine-regioner",
"nlpengine-context",
"nlpengine-hdd",
"nlpengine-constraint-engine",
"uima",
]

projects_without_uima = [
"nlpengine-ctakes",
"nlpengine-common",
"nlpengine-preprocessing",
"nlpengine-measurements",
"nlpengine-dictionary",
"nlpengine-parser",
"nlpengine-doctype",
"nlpengine-wsd",
"nlpengine-regioner",
"nlpengine-context",
"nlpengine-hdd",
"nlpengine-constraint-engine",
]