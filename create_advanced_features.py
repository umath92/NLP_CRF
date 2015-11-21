#!/usr/bin/env python3

import sys
from decimal import *
import math
import copy


"""hw3_corpus_tools.py: CSCI544 Homework 3 Corpus Code

USC Computer Science 544: Applied Natural Language Processing

Provides two functions and two data containers:
get_utterances_from_file - loads utterances from an open csv file
get_utterances_from_filename - loads utterances from a filename
DialogUtterance - A namedtuple with various utterance attributes
PosTag - A namedtuple breaking down a token/pos pair

This code is provided for your convenience. You are not required to use it.
Feel free to import, edit, copy, and/or rename to use in your assignment.
Do not distribute."""

__author__ = "Christopher Wienberg"
__email__ = "cwienber@usc.edu"

from collections import namedtuple
import csv
import glob
import os

def get_utterances_from_file(dialog_csv_file):
    """Returns a list of DialogUtterances from an open file."""
    reader = csv.DictReader(dialog_csv_file)
    return [_dict_to_dialog_utterance(du_dict) for du_dict in reader]

def get_utterances_from_filename(dialog_csv_filename):
    """Returns a list of DialogUtterances from an unopened filename."""
    with open(dialog_csv_filename, "r") as dialog_csv_file:
        return get_utterances_from_file(dialog_csv_file)

DialogUtterance = namedtuple(
    "DialogUtterance", ("act_tag", "speaker", "pos", "text"))

DialogUtterance.__doc__ = """\
An utterance in a dialog. Empty utterances are None.

act_tag - the dialog act associated with this utterance
speaker - which speaker made this utterance
pos - a list of PosTag objects (token and POS)
text - the text of the utterance with only a little bit of cleaning"""

PosTag = namedtuple("PosTag", ("token", "pos"))

PosTag.__doc__ = """\
A token and its part-of-speech tag.

token - the token
pos - the part-of-speech tag"""

def _dict_to_dialog_utterance(du_dict):
    """Private method for converting a dict to a DialogUtterance."""

    # Remove anything with 
    for k, v in du_dict.items():
        if len(v.strip()) == 0:
            du_dict[k] = None

    # Extract tokens and POS tags
    if du_dict["pos"]:
        du_dict["pos"] = [
            PosTag(*token_pos_pair.split("/"))
            for token_pos_pair in du_dict["pos"].split()]
    return DialogUtterance(**du_dict)


# My code..

filename=sys.argv[1]



#first one so not storing speaker.



speaker_first="";
qsn_first=0;
firstRun=True
list0=get_utterances_from_filename(filename)
for list1 in list0:
    if(firstRun==True):
        speaker_first=list1.speaker
        if(list1.act_tag!=None):
            line=list1.act_tag+"\t"+"YES"+"\t"
        else:
            line="qw"+"\t"+"YES"+"\t"
        firstRun=False
        line=line+"0"+"\t"
    else:
        if(list1.act_tag!=None):
            line=list1.act_tag+"\t"+"NO"+"\t"
        else:
            line="qw"+"\t"+"NO"+"\t"

        if(speaker_first!=list1.speaker):
            line=line+"1"+"\t"
        else:
            line=line+"0"+"\t"
        speaker_first=list1.speaker
    line=line+list1.speaker+"\t"

    # token and pos feature. if not there -- skip.
    if (list1.pos!=None):
        for i in list1.pos:
                line=line+"TOKEN_"+i.token+"\t"
                line=line+"POS_"+i.pos+"\t"
                if(i.token=="?"):
                    line=line+"TAG_question"+"\t"
                    qsn_first=1
        # bi grams and tri grams

        pre="BIGRAM_"
        tri1="TRIGRAM_"
        tri2=""
        f1=1
        f2=2
        for i in list1.pos:
            line=line+pre+"_"+i.token+"\t"
            pre="BIGRAM_"+i.token
            if(f1==1):
                tri1="TRIGRAM_"+i.token
                f1=0
            elif(f2==2):
                tri2=i.token
                f2=0
            else:
                line=line+tri1+"_"+tri2+"_"+i.token+"\t"
                tri1="TRIGRAM_"+tri2
                tri2=i.token
                

        # bi grams and tri grams

        if(qsn_first==0):
            line=line+"TAG_answer"+"\t"
        qsn_first=0
    else:
        line=line+"TOKEN_Empty"+"\t"
        line=line+"POS_Empty"+"\t"

    l=list1.text
    l=l.replace(":","")
    l=l.replace("\\","")
    l=l.replace(" ","\t")
    line=line+l

    line=line.rstrip()
    print(line)
print()





