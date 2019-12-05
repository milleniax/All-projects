import pandas as pd
import xml.etree.cElementTree as et


def getvalueofnode(node):
    """ return node text or None """
    return node.text if node is not None else None

def main():
    parsedXML = et.parse('map.osm')
    dfcols = ['id', 'uid', 'timestamp', 'lat', 'lon']
    df_xml = pd.DataFrame(columns=dfcols)

    for node in parsedXML.getroot():
        id = node.attrib.get('id')
        uid = node.attrib.get('uid')
        timestamp = node.attrib.get('timestamp')
        lat = node.attrib.get('lat')
        lon = node.attrib.get('lon')

        df_xml = df_xml.append(
            pd.Series([id, uid, timestamp, lat, lon], index=dfcols),
            ignore_index=True)

        # print(df_xml)
    print(df_xml.head())

main()
