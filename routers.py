from fastapi import APIRouter, Depends, HTTPException
import pickle
import schemas as cln

router = APIRouter(
    prefix="/predict",
    tags=["/predict"],
    responses={404: {"description": "Not found"}},
)


''' PREDICT PRICE '''


@router.post("/predict")
async def predict(credential: cln.House):
    model = pickle.load(open('linear_reg.pkl', 'rb'))
    makeprediction = model.predict(
        [[credential.AvgAreaIncome, credential.AvgAreaHouseAge, credential.AvgAreaNumberofRooms, credential.AvgAreaNumberofBedrooms, credential.AreaPopulation]])
    if len(makeprediction):
        return cln.HouseResult(status=True, message="succes", result=makeprediction[0],
                               house=cln.House(AvgAreaIncome=credential.AvgAreaIncome,
                                               AvgAreaHouseAge=credential.AvgAreaHouseAge,
                                               AvgAreaNumberofRooms=credential.AvgAreaNumberofRooms,
                                               AvgAreaNumberofBedrooms=credential.AvgAreaNumberofBedrooms,
                                               AreaPopulation=credential.AreaPopulation,
                                               Price=round(
                                                   makeprediction[0], 2) if makeprediction[0] > 0 else 0
                                               ))
    else:
        return cln.HouseResult(status=False, message="error", result=0,
                               house=cln.House(AvgAreaIncome=0,
                                               AvgAreaHouseAge=0,
                                               AvgAreaNumberofRooms=0,
                                               AvgAreaNumberofBedrooms=0,
                                               AreaPopulation=0,
                                               Price=0
                                               ))
