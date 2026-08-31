class Fountain:
    def __init__(self, objectid, lat, lon, basis_typ, basis_typ_txt): 
        self.objectid = objectid
        self.lat = lat
        self.lon = lon
        self.basis_typ = basis_typ
        self.basis_typ_txt = basis_typ_txt
    def __repr__(self):
        return f"Fountain({self.objectid}, {self.lat}, {self.lon}, {self.basis_typ}, {self.basis_typ_txt})"


