# 2.1.1 METADATA FORMAT (.inv file)
# Variable          Columns      Type
# --------          -------      ----
# ID                 1-11        Integer
# LATITUDE          13-20        Real
# LONGITUDE         22-30        Real
# STNELEV           32-37        Real
# NAME              39-68        Character

# Variable Definitions:
# ID: Station identification code. First two characters are FIPS country code
# LATITUDE: latitude of station in decimal degrees
# LONGITUDE: longitude of station in decimal degrees
# STELEV: is the station elevation in meters. -999.0 = missing.
# NAME: station name

# Example data
# MX000005033	27.87	-101.28	340	SABINAS
# MX000005042	28.5	-100.92	400	ZARAGOZA
# MX000005044	26.98	-102.07	0	CUATRO_CIENEGAS
# MX000005045	27.62	-100.72	305	VILLA_JUAREZ
# MX000005047	26.883	-101.433	615	MONCLOVA

data = {
    "stations": [
        {
            "id": "MX000005033",
            "latitude": "27.87",
            "longitude": "-101.28",
            "elevation": "340",
            "name": "SABINAS",
        },
        {
            "id": "MX000005042",
            "latitude": "28.5",
            "longitude": "-100.92",
            "elevation": "400",
            "name": "ZARAGOZA",
        },
        {
            "id": "MX000005045",
            "latitude": "27.62",
            "longitude": "-100.72",
            "elevation": "305",
            "name": "VILLA_JUAREZ",
        },
        {
            "id": "MX000005047",
            "latitude": "26.883",
            "longitude": "-101.433",
            "elevation": "615",
            "name": "MONCLOVA",
        },
        {
            "id": "MX000005044",
            "latitude": "26.98",
            "longitude": "-102.07",
            "elevation": "0",
            "name": "CUATRO_CIENEGAS",
        },
        {
            "id": "MX000003073",
            "latitude": "26.564397",
            "longitude": "-102.262833",
            "elevation": "0",
            "name": "GUSTAVO_DIAZ_ORDAZ",
        },
        {
            "id": "MX000004011",
            "latitude": "20.18",
            "longitude": "-90.13",
            "elevation": "50",
            "name": "HECELCHAKAN",
        },
        {
            "id": "MX000004001",
            "latitude": "20",
            "longitude": "-89.82",
            "elevation": "0",
            "name": "BOLONCHEN",
        },
        {
            "id": "MX000004004",
            "latitude": "18.18",
            "longitude": "-91.05",
            "elevation": "25",
            "name": "CANDELARIA",
        },
        {
            "id": "MXM00076519",
            "latitude": "22.1",
            "longitude": "-103.267",
            "elevation": "1673",
            "name": "COLOTLANJAL",
        },
        {
            "id": "MXM00076525",
            "latitude": "22.783",
            "longitude": "-102.567",
            "elevation": "2612",
            "name": "ZACATECASZAC_LA_BUFAZAC",
        },
        {
            "id": "MXM00076539",
            "latitude": "22.254",
            "longitude": "-100.931",
            "elevation": "1839.5",
            "name": "PONCIANO_ARRIAGA_INTL",
        },
        {
            "id": "MXM00076499",
            "latitude": "23.767",
            "longitude": "-98.2",
            "elevation": "21",
            "name": "SOTO_LA_MARINATAMPS",
        },
        {
            "id": "MXM00076543",
            "latitude": "22",
            "longitude": "-98.767",
            "elevation": "104",
            "name": "TAMUINSLP",
        },
        {
            "id": "MXM00076545",
            "latitude": "21.983",
            "longitude": "-99.017",
            "elevation": "0",
            "name": "EL_NARANJO_SLP",
        },
        {
            "id": "MXM00076547",
            "latitude": "21.983",
            "longitude": "-99.017",
            "elevation": "0",
            "name": "EL_NARANJO_SLP",
        },
        {
            "id": "MX000003074",
            "latitude": "22.157159",
            "longitude": "-98.840830",
            "elevation": "18",
            "name": "LA_PAZ_CITY",
        },
        {
            "id": "MXM00076549",
            "latitude": "21.983",
            "longitude": "-99.017",
            "elevation": "0",
            "name": "EL_NARANJO_SLP",
        },
    ]
}
