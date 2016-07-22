#!/usr/bin/env python
#

import ujson as json

def clean_poi(d):
    with open('clean_poi.json', 'w') as outfile:
        for entry in d:
            new_entry = {"id":entry['id'],
                         "categories":entry['categories'],
                         "border_points":entry['border_points'],
                         "poi_label":entry['poi_label'],
                         "stars":entry['stars'],
                         "dist_to_poi":0,
                         "type":"POI"}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_bp(d):
    with open('clean_bp.json', 'w') as outfile:
        for entry in d:
            new_entry = {"id":int(entry['id']),
                         "categories":[""],
                         "border_points":[""],
                         "poi_label":"",
                         "stars":"",
                         "dist_to_poi":entry['dist_to_poi'],
                         "type":"BP"}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_node(d):
    with open('clean_node.json', 'w') as outfile:
        for entry in d:
            new_entry = {"id":entry['id'],
                         "categories":[""],
                         "border_points":[""],
                         "poi_label":entry['poi_label'],
                         "stars":"",
                         "dist_to_poi":entry['dist_to_poi'],
                         "type":"node"}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_vertices(d):
    with open('newG1Vertices.json', 'w') as outfile:
        for entry in d:
            new_entry = {"id":float(entry['id']),
                         "categories":entry['categories'],
                         "border_points":entry['border_points'],
                         "poi_label":float(entry['poi_label']),
                         "stars":entry['stars'],
                         "dist_to_poi":entry['dist_to_poi'],
                         "type":entry['type']}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_vertices2(d):
    with open('newG2Vertices.json', 'w') as outfile:
        for entry in d:
            new_entry = {"id":float(entry['id']),
                         "categories":entry['categories'],
                         "border_points":entry['border_points'],
                         "poi_label":float(entry['poi_label']),
                         "stars":entry['stars'],
                         "dist_to_poi":entry['dist_to_poi'],
                         "type":entry['type']}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_edge(d):
    with open('newG1Edges.json', 'w') as outfile:
        for entry in d:
            new_entry = {"dst":float(entry['dst']),
                         "src":float(entry['src']),
                         "weight":entry['weight']}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_edge2(d):
    with open('newG2Edges.json', 'w') as outfile:
        for entry in d:
            new_entry = {"dst":float(entry['dst']),
                         "src":float(entry['src']),
                         "weight":entry['weight']}
            out = json.dumps(new_entry,double_precision=35)
            outfile.write(out + ',\n')

def clean_vertices_array(d):
    with open('G1Vertices.json', 'w') as outfile:
        for entry in d:
            if entry['border_points'] != [""]:
                new_bp = []
                for bp in entry['border_points']:
                    new_bp.append(float(bp))
                new_entry = {"id":entry['id'],
                             "categories":entry['categories'],
                             "border_points":new_bp,
                             "poi_label":entry['poi_label'],
                             "stars":entry['stars'],
                             "dist_to_poi":entry['dist_to_poi'],
                             "type":entry['type']}
                out = json.dumps(new_entry,double_precision=35)
                outfile.write(out + ',\n')
            else:
                new_entry = {"id":entry['id'],
                             "categories":entry['categories'],
                             "border_points":entry['border_points'],
                             "poi_label":entry['poi_label'],
                             "stars":entry['stars'],
                             "dist_to_poi":entry['dist_to_poi'],
                             "type":entry['type']}
                out = json.dumps(new_entry,double_precision=35)
                outfile.write(out + ',\n')

def clean_vertices_test(d):
    with open('G1Vertices.json', 'w') as outfile:
        for entry in d:
            if entry['border_points'] != [""]:
                new_bp = []
                for bp in entry['border_points']:
                    new_bp.append(float(bp))
                new_entry = {"id":float(entry['id']),
                             "categories":entry['categories'],
                             "border_points":new_bp,
                             "poi_label":float(entry['poi_label']),
                             "stars":entry['stars'],
                             "dist_to_poi":float(entry['dist_to_poi']),
                             "type":entry['type']}
                out = json.dumps(new_entry,double_precision=35)
                outfile.write(out + ',\n')
            elif entry['type'] == "node":
                new_entry = {"id":float(entry['id']),
                             "categories":entry['categories'],
                             "border_points":entry['border_points'],
                             "poi_label":float(entry['poi_label']),
                             "stars":0.0,
                             "dist_to_poi":float(entry['dist_to_poi']),
                             "type":entry['type']}
                out = json.dumps(new_entry,double_precision=35)
                outfile.write(out + ',\n')
            else:
                new_entry = {"id":float(entry['id']),
                             "categories":entry['categories'],
                             "border_points":entry['border_points'],
                             "poi_label":0.0,
                             "stars":0.0,
                             "dist_to_poi":float(entry['dist_to_poi']),
                             "type":entry['type']}
                out = json.dumps(new_entry,double_precision=35)
                outfile.write(out + ',\n')

if __name__=='__main__':
    #for border points, if not == [""], then add '.0' after each entry
    vjson = open('TestVertices2.json','r+').read().decode("utf-8")
    vdata = json.loads(vjson)

    clean_vertices_test(vdata)

    """
    vjson_d1 = open('TestVertices.json','r+').read().decode("utf-8")
    vdata = json.loads(vjson_d1)

    vjson_d2 = open('TestVertices2.json','r+').read().decode("utf-8")
    vdata2 = json.loads(vjson_d2)


    ejson_d1 = open('TestEdges.json','r+').read().decode("utf-8")
    edata = json.loads(ejson_d1)

    ejson_d2 = open('TestEdges2.json','r+').read().decode("utf-8")
    edata2 = json.loads(ejson_d2)


    clean_vertices(vdata)
    clean_vertices2(vdata2)
    clean_edge(edata)
    clean_edge2(edata2)
    

    pjson_data = open('TestPOI.json','r+').read().decode("utf-8")
    pdata = json.loads(pjson_data)

    bjson_data = open('TestBP.json','r+').read().decode("utf-8")
    bdata = json.loads(bjson_data)

    njson_data = open('TestNode.json','r+').read().decode("utf-8")
    ndata = json.loads(njson_data)

    pjson_data = open('tidy_POI.json','r+').read().decode("utf-8")
    pdata = json.loads(pjson_data)

    bjson_data = open('tidy_BP.json','r+').read().decode("utf-8")
    bdata = json.loads(bjson_data)

    njson_data = open('G1Node.json','r+').read().decode("utf-8")
    ndata = json.loads(njson_data)

    ejson_data = open('TestEdges2.json','r+').read().decode("utf-8")
    edata = json.loads(ejson_data)

    clean_poi(pdata)
    clean_bp(bdata)
    clean_node(ndata)
    clean_edge(edata)
    """
