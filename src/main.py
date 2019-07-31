import googlemaps
import gmplot
import re
import os
import requests

gmaps = googlemaps.Client(key=os.environ['MAPS_API_KEY'])


def get_enterprises():
    """
    Logs to intranet with a POST method submitting the form fields and then makes a GET method,
    and searchs for a pattern in order to get a list of the enterprises

    :return:The list containing the enterprises
    """
    url = 'https://intranet.etsetb.upc.edu/serveis/estudiants/relacions_externes/llistat_empreses.html'
    url_login = 'https://intranet.etsetb.upc.edu/sys/login.html'
    payload = {'login': os.environ['UPC_USER'],'password': os.environ['UPC_PASS'],'submit':'inici de Sessió'}

    with requests.Session() as s:
        s.post(url_login, data=payload)
        res = s.get(url)
        data = re.findall('<tr><.*">(.*)</td', res.text)
        return data


def parse_name_to_marker(enterprises):
    """
    Uses google maps API in order to obtain get the closest address to Barcelona from each
    enterprise office in the list it also gets its website and displays the info in the map with a
    marker.
    :param enterprises:  the list of enterprises that we want to allocate in the map
    """
    gmap = gmplot.GoogleMapPlotter(41.39021337, 2.1357438,13, os.environ['MAPS_API_KEY'])
    addr = []
    for enterp in enterprises:
        print("Parsing", enterp)
        addr_tmp = gmaps.places(query=enterp, location=(41.39021337, 2.1357438))
        if addr_tmp['status'] == 'OK':
            addr.append(addr_tmp['results'][0]['formatted_address'])
            website = gmaps.place(addr_tmp['results'][0]['place_id'], fields=['website'])['result']
            if bool(website):
                gmap.marker(addr_tmp['results'][0]['geometry']['location']['lat'],
                            addr_tmp['results'][0]['geometry']['location']['lng'],
                            title=("<b><u>" + enterp +"</u></b>"), label=("<br /> <b>Website :</b> "
                                   + "<a href=" + website['website']+">"+website['website']+"</a>"))
            else:
                gmap.marker(addr_tmp['results'][0]['geometry']['location']['lat'],
                            addr_tmp['results'][0]['geometry']['location']['lng'],
                            title=("<b><u>" + enterp + "</u></b>"), label="<br/> No website found")
    print("Ended parsing and querying")
    gmap.draw(os.path.dirname(os.path.dirname(__file__))+'map/map.html')


if __name__ == "__main__":
    enterprises = get_enterprises()
    parse_name_to_marker(enterprises)
