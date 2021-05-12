from enum import Enum
from typing import Set, Dict

class Cities(Enum):
    # Blue
    SanFrancisco = "San Francisco"
    Chicago = "Chicago"
    Montreal = "Montreal"
    NewYork = "New York"
    Atlanta = "Atlanta"
    Washington = "Washington"
    London = "London"
    Essen = "Essen"
    StPetersburg = "St. Petersburg"
    Madrid = "Madrid"
    Paris = "Paris"
    Milan = "Milan"
    # Yellow
    LosAngeles = "Los Angeles"
    MexicoCity = "Mexico City"
    Miami = "Miami"
    Bogota = "Bogota"
    Lima = "Lima"
    Santiago = "Santiago"
    BuenosAries = "Buenos Aries"
    SaoPaulo = "Sao Paulo"
    Lagos = "Lagos"
    Khartoum = "Khartoum"
    Kinshasa = "Kinshasa"
    Johannesburg = "Johannesburg"
    # Black
    Moscow = "Moscow"
    Istanbul = "Istanbul"
    Tehran = "Tehran"
    Algiers = "Algiers"
    Baghdad = "Baghdad"
    Delhi = "Delhi"
    Cairo = "Cairo"
    Karachi = "Karachi"
    Kolkata = "Kolkata"
    Riyadh = "Riyadh"
    Mumbai = "Mumbai"
    Chennai = "Chennai"
    # Red
    Beijing = "Beijing"
    Seoul = "Seoul"
    Shanghai = "Shanghai"
    Tokyo = "Tokyo"
    BangKok = "Bangkok"
    HongKong = "Hong Kong"
    Taipei = "Taipei"
    Osaka = "Osaka"
    HoChiMinhCity = "Ho Chi Minh City"
    Manila = "Manila"
    Jakarta = "Jakarta"
    Sydney = "Sydney"

class SpecialCards(Enum):
    Infection = "Infection"

class Diseases(Enum):
    Blue = "Blue"
    Yellow = "Yellow"
    Black = "Black"
    Red = "Red"

CitiesInPlay = {
    # Blue
    Cities.SanFrancisco, Cities.Chicago, Cities.Montreal, Cities.NewYork, Cities.Atlanta, Cities.Washington, Cities.London, Cities.Essen, Cities.StPetersburg, Cities.Madrid, Cities.Paris, Cities.Milan,
    # Yellow
    Cities.LosAngeles, Cities.MexicoCity, Cities.Miami, Cities.Bogota, Cities.Lima, Cities.Santiago, Cities.BuenosAries, Cities.SaoPaulo, Cities.Lagos, Cities.Khartoum, Cities.Kinshasa, Cities.Johannesburg, 
    # Black
    Cities.Moscow, Cities.Istanbul, Cities.Tehran, Cities.Algiers, Cities.Baghdad, Cities.Delhi, Cities.Cairo, Cities.Karachi, Cities.Kolkata, Cities.Riyadh, Cities.Mumbai, Cities.Chennai, 
    # Red
    Cities.Beijing, Cities.Seoul, Cities.Shanghai, Cities.Tokyo, Cities.BangKok, Cities.HongKong, Cities.Taipei, Cities.Osaka, Cities.HoChiMinhCity, Cities.Manila, Cities.Jakarta, Cities.Sydney,
}

DiseasesInPlay = {
    Diseases.Blue,
    Diseases.Yellow,
    Diseases.Black,
    Diseases.Red,
}

MaxOutbreaks = 8
MaxCubes = {
    Diseases.Blue: 24,
    Diseases.Yellow: 24,
    Diseases.Black: 24,
    Diseases.Red: 24,
}
InfectionRate = [2,2,2,3,3,4,4]
    
CitiesConnections = {
    # Blue
    Cities.SanFrancisco: {Cities.Tokyo, Cities.Manila, Cities.Chicago, Cities.LosAngeles},
    Cities.Chicago: {Cities.SanFrancisco, Cities.LosAngeles, Cities.MexicoCity, Cities.Atlanta, Cities.Montreal},
    Cities.Montreal: {Cities.Chicago, Cities.Washington, Cities.NewYork},
    Cities.NewYork: {Cities.Montreal, Cities.Washington, Cities.London, Cities.Madrid},
    Cities.Atlanta: {Cities.Chicago, Cities.Miami, Cities.Washington},
    Cities.Washington: {Cities.Atlanta, Cities.Miami, Cities.Montreal, Cities.NewYork},
    Cities.London: {Cities.NewYork, Cities.Madrid, Cities.Paris, Cities.Essen},
    Cities.Essen: {Cities.London, Cities.Paris, Cities.Milan, Cities.StPetersburg},
    Cities.StPetersburg: {Cities.Essen, Cities.Istanbul, Cities.Moscow},
    Cities.Madrid: {Cities.NewYork, Cities.SaoPaulo, Cities.Algiers, Cities.Paris, Cities.London},
    Cities.Paris: {Cities.London, Cities.Essen, Cities.Madrid, Cities.Milan, Cities.Algiers},
    Cities.Milan: {Cities.Essen, Cities.Paris, Cities.Istanbul},
    # Yellow
    Cities.LosAngeles: {Cities.Sydney, Cities.MexicoCity, Cities.SanFrancisco, Cities.Chicago},
    Cities.MexicoCity: {Cities.LosAngeles, Cities.Chicago, Cities.Miami, Cities.Bogota, Cities.Lima},
    Cities.Miami: {Cities.Atlanta, Cities.Washington, Cities.Bogota, Cities.MexicoCity},
    Cities.Bogota: {Cities.MexicoCity, Cities.Miami, Cities.Lima, Cities.SaoPaulo, Cities.BuenosAries},
    Cities.Lima: {Cities.MexicoCity, Cities.Bogota, Cities.Santiago},
    Cities.Santiago: {Cities.Lima},
    Cities.BuenosAries: {Cities.Bogota, Cities.SaoPaulo},
    Cities.SaoPaulo: {Cities.Bogota, Cities.BuenosAries, Cities.Lagos, Cities.Madrid},
    Cities.Lagos: {Cities.SaoPaulo, Cities.Khartoum, Cities.Kinshasa},
    Cities.Khartoum: {Cities.Lagos, Cities.Kinshasa, Cities.Johannesburg, Cities.Cairo},
    Cities.Kinshasa: {Cities.Lagos, Cities.Khartoum, Cities.Johannesburg},
    Cities.Johannesburg: {Cities.Kinshasa, Cities.Khartoum},
    # Black
    Cities.Moscow: {Cities.StPetersburg, Cities.Istanbul, Cities.Tehran},
    Cities.Istanbul: {Cities.StPetersburg, Cities.Moscow, Cities.Baghdad, Cities.Algiers, Cities.Milan, Cities.Cairo},
    Cities.Tehran: {Cities.Moscow, Cities.Baghdad, Cities.Delhi, Cities.Karachi},
    Cities.Algiers: {Cities.Madrid, Cities.Paris, Cities.Istanbul, Cities.Cairo},
    Cities.Baghdad: {Cities.Istanbul, Cities.Cairo, Cities.Riyadh, Cities.Tehran, Cities.Karachi},
    Cities.Delhi: {Cities.Tehran, Cities.Karachi, Cities.Mumbai, Cities.Chennai, Cities.Kolkata},
    Cities.Cairo: {Cities.Algiers, Cities.Istanbul, Cities.Baghdad, Cities.Riyadh, Cities.Khartoum},
    Cities.Karachi: {Cities.Tehran, Cities.Baghdad, Cities.Riyadh, Cities.Mumbai, Cities.Delhi},
    Cities.Kolkata: {Cities.Delhi, Cities.Chennai, Cities.BangKok, Cities.HongKong},
    Cities.Riyadh: {Cities.Cairo, Cities.Baghdad, Cities.Karachi},
    Cities.Mumbai: {Cities.Karachi, Cities.Delhi, Cities.Chennai},
    Cities.Chennai: {Cities.Mumbai, Cities.Delhi, Cities.Kolkata, Cities.BangKok, Cities.Jakarta},
    # Red
    Cities.Beijing: {Cities.Seoul, Cities.Shanghai},
    Cities.Seoul: {Cities.Beijing, Cities.Tokyo, Cities.Shanghai},
    Cities.Shanghai: {Cities.Beijing, Cities.Seoul, Cities.Tokyo, Cities.Taipei, Cities.HongKong},
    Cities.Tokyo: {Cities.Seoul, Cities.Shanghai, Cities.Osaka, Cities.SanFrancisco},
    Cities.BangKok: {Cities.Kolkata, Cities.Chennai, Cities.Jakarta, Cities.HoChiMinhCity, Cities.HongKong},
    Cities.HongKong: {Cities.Kolkata, Cities.BangKok, Cities.HoChiMinhCity, Cities.Manila, Cities.Taipei, Cities.Shanghai},
    Cities.Taipei: {Cities.HongKong, Cities.Shanghai, Cities.Osaka, Cities.Manila},
    Cities.Osaka: {Cities.Tokyo, Cities.Taipei},
    Cities.HoChiMinhCity: {Cities.BangKok, Cities.HongKong, Cities.Manila, Cities.Jakarta},
    Cities.Manila: {Cities.Sydney, Cities.SanFrancisco, Cities.Taipei, Cities.HongKong, Cities.HoChiMinhCity},
    Cities.Jakarta: {Cities.Chennai, Cities.BangKok, Cities.HoChiMinhCity, Cities.Sydney},
    Cities.Sydney: {Cities.Jakarta, Cities.Manila, Cities.LosAngeles},
}

CitiesDiseases = {
    # Blue
    Cities.SanFrancisco: Diseases.Blue,
    Cities.Chicago: Diseases.Blue,
    Cities.Montreal: Diseases.Blue,
    Cities.NewYork: Diseases.Blue,
    Cities.Atlanta: Diseases.Blue,
    Cities.Washington: Diseases.Blue,
    Cities.London: Diseases.Blue,
    Cities.Essen: Diseases.Blue,
    Cities.StPetersburg: Diseases.Blue,
    Cities.Madrid: Diseases.Blue,
    Cities.Paris: Diseases.Blue,
    Cities.Milan: Diseases.Blue,
    # Yellow
    Cities.LosAngeles: Diseases.Yellow,
    Cities.MexicoCity: Diseases.Yellow,
    Cities.Miami: Diseases.Yellow,
    Cities.Bogota: Diseases.Yellow,
    Cities.Lima: Diseases.Yellow,
    Cities.Santiago: Diseases.Yellow,
    Cities.BuenosAries: Diseases.Yellow,
    Cities.SaoPaulo: Diseases.Yellow,
    Cities.Lagos: Diseases.Yellow,
    Cities.Khartoum: Diseases.Yellow,
    Cities.Kinshasa: Diseases.Yellow,
    Cities.Johannesburg: Diseases.Yellow,
    # Black
    Cities.Moscow: Diseases.Black,
    Cities.Istanbul: Diseases.Black,
    Cities.Tehran: Diseases.Black,
    Cities.Algiers: Diseases.Black,
    Cities.Baghdad: Diseases.Black,
    Cities.Delhi: Diseases.Black,
    Cities.Cairo: Diseases.Black,
    Cities.Karachi: Diseases.Black,
    Cities.Kolkata: Diseases.Black,
    Cities.Riyadh: Diseases.Black,
    Cities.Mumbai: Diseases.Black,
    Cities.Chennai: Diseases.Black,
    # Red
    Cities.Beijing: Diseases.Red,
    Cities.Seoul: Diseases.Red,
    Cities.Shanghai: Diseases.Red,
    Cities.Tokyo: Diseases.Red,
    Cities.BangKok: Diseases.Red,
    Cities.HongKong: Diseases.Red,
    Cities.Taipei: Diseases.Red,
    Cities.Osaka: Diseases.Red,
    Cities.HoChiMinhCity: Diseases.Red,
    Cities.Manila: Diseases.Red,
    Cities.Jakarta: Diseases.Red,
    Cities.Sydney: Diseases.Red,
}