#!/usr/bin/env python

#### Write a BioC collection in JSON

from __future__ import print_function

import json
import sys
import os

pybioc_path = '/home/comeau/src/PyBioC'
sys.path.append(os.path.join(pybioc_path, 'src'))
import bioc

class BioC2JSON:
    def node(this, node):
        json_node = {'refid': node.refid, 'role': node.role}
        return json_node
    
    def relation(this, rel):
        json_rel = {}
        json_rel['id'] = rel.id
        json_rel['infons'] = rel.infons
        json_rel['nodes'] = [this.node(n) for n in rel.nodes] 
        return json_rel

    def location(this, loc):
        json_loc = {'offset': int(loc.offset), 'length': int(loc.length)}
        return json_loc

    def annotation(this, note):
        json_note = {}
        json_note['id'] = note.id
        json_note['infons'] = note.infons
        json_note['text'] = note.text
        json_note['locations'] = [this.location(l)
                                  for l in note.locations] 
        return json_note
    
    def sentence(this, sent):
        json_sent = {}
        json_sent['infons'] = sent.infons
        json_sent['offset'] = int(sent.offset)
        json_sent['text'] = sent.text
        json_sent['annotations'] = [this.annotation(a)
                                    for a in sent.annotations]
        json_sent['relations'] = [this.relation(r)
                                  for r in sent.relations] 
        return json_sent

    def passage(this, psg):
        json_psg = {}
        json_psg['infons'] = psg.infons
        json_psg['offset'] = int(psg.offset)
        json_psg['text'] =  psg.text
        json_psg['text'] =  psg.text if psg.text else ""
        json_psg['sentences'] = [this.sentence(s)
                                 for s in psg.sentences] 
        json_psg['annotations'] = [this.annotation(a)
                                   for a in psg.annotations]
        json_psg['relations'] = [this.relation(r)
                                 for r in psg.relations] 
        return json_psg

    def document(this, doc):
        json_doc = {}
        json_doc['id'] = doc.id
        json_doc['infons'] = doc.infons
        json_doc['passages'] = [this.passage(p)
                                for p in doc.passages]
        json_doc['relations'] = [this.relation(r)
                                 for r in doc.relations] 
        return json_doc

    def collection(this, collection):
        json_collection = {}
        json_collection['source'] = collection.source
        json_collection['date'] = collection.date
        json_collection['key'] = collection.key
        json_collection['infons'] = collection.infons
        json_collection['documents'] = [this.document(d)
                                        for d in collection.documents] 
        return json_collection

class JSON2BioC:

    def node(this, json_node):
        node = bioc.BioCNode()
        node.refid = json_node['refid']
        node.role = json_node['role']
        return node

    def relation(this, json_rel):
        rel = bioc.BioCRelation()
        rel.id = json_rel['id']
        rel.infons = json_rel['infons']
        rel.nodes = [this.node(n) for n in json_rel['nodes']] 
        return rel

    def location(this, json_loc):
        loc = bioc.BioCLocation()
        loc.offset = str(json_loc['offset'])
        loc.length = str(json_loc['length'])
        return loc

    def annotation(this, json_note):
        note = bioc.BioCAnnotation()
        note.id = json_note['id']
        note.infons = json_note['infons']
        note.text = json_note['text']
        note.locations = [this.location(l)
                          for l in json_note['locations']] 
        return note
    
    def sentence(this, json_sent):
        sent = bioc.BioCSentence()
        sent.infons = json_sent['infons']
        sent.offset = str(json_sent['offset'])
        sent.text = json_sent['text']
        sent.annotations = [this.annotation(a)
                            for a in json_sent['annotations']]
        sent.relations = [this.relation(r)
                          for r in json_sent['relations']]
        return sent

    def passage(this, json_psg):
        psg = bioc.BioCPassage()
        psg.infons = json_psg['infons']
        psg.offset = str(json_psg['offset'])
        psg.text = json_psg.get('text')
        psg.sentences = [this.sentence(s)
                         for s in json_psg['sentences']]
        psg.annotations = [this.annotation(a)
                           for a in json_psg['annotations']]
        psg.relations = [this.relation(r)
                         for r in json_psg['relations']]
        return psg

    def document(this, json_doc):
        doc = bioc.BioCDocument()
        doc.id = json_doc['id']
        doc.infons = json_doc['infons']
        doc.passages = [this.passage(p)
                        for p in json_doc['passages']]
        doc.relations = [this.relation(r)
                         for r in json_doc['relations']]
        return doc

    def collection(this, json_collection):
        collection = bioc.BioCCollection()
        collection.source = json_collection['source']
        collection.date = json_collection['date'] 
        collection.key = json_collection['key']
        collection.infons = json_collection['infons']
        collection.documents = [this.document(d)
                                for d in json_collection['documents']]
        return collection

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print('usage:', sys.argv[0], '-b|-j in_file out_file')
        exit(1)
    pgm, option, in_file, out_file = sys.argv

    if option == '-j':
        reader = bioc.BioCReader(in_file)
        reader.read()

        bioc2json = BioC2JSON()
        bioc_json = bioc2json.collection(reader.collection)
        with open(out_file, 'w') as f:
            json.dump(bioc_json, f, indent=2)
            print(file=f)

    elif option == '-b':
        bioc_json = None
        with open(in_file) as f:
            bioc_json = json.load(f)

        # print json.dumps(bioc_json, indent=2)

        json2bioc =JSON2BioC()
        bioc_collection = json2bioc.collection(bioc_json)
        
        writer = bioc.BioCWriter(out_file, bioc_collection)
        writer.write()
