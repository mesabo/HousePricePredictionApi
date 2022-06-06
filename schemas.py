from typing import Optional, List
from numpy import float64
from pydantic import BaseModel


class House(BaseModel):
    AvgAreaIncome: Optional[float64] = 61907
    AvgAreaHouseAge: Optional[float64] = 7
    AvgAreaNumberofRooms: Optional[float64] = 6
    AvgAreaNumberofBedrooms: Optional[float64] = 3
    AreaPopulation: Optional[float64] = 43828
    Price: Optional[float64] = 1252209.97
    # message: Optional[str] = "Le prix de cet appartement est estimé à "

    class Config:
        schema_extra = {
            "example": {
                "AvgAreaIncome": 61907,
                "AvgAreaHouseAge": 7,
                "AvgAreaNumberofRooms": 6,
                "AvgAreaNumberofBedrooms": 3,
                "AreaPopulation": 43828,
                "Price": 1252209.97,
            }
        }


class HouseResult(BaseModel):
    status: Optional[bool] = True
    message: Optional[str] = "succes"
    result: Optional[float64] = 7000,
    house: House

    class Config:
        schema_extra = {
            "example": {
                "status": True,
                "message": "success",
                "result": 252209.97,
                "house": {
                "AvgAreaIncome": 61907,
                "AvgAreaHouseAge": 7,
                "AvgAreaNumberofRooms": 6,
                "AvgAreaNumberofBedrooms": 3,
                "AreaPopulation": 43828,
                "Price": 1252209.97,
            }
            }
        }
