from typing import Optional
import fastapi
import httpx
from models.location import Location
from models.umbrella_status import UmbrellaStatus

router = fastapi.APIRouter()

@router.get('/api/umbrella', response_model = UmbrellaStatus)
#Dependency injection
async def needUmbrella(location: Location = fastapi.Depends()):
    url = f'https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}&units=imperial'
    if location.state:
        url+=f'&state={location.state}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

        data = response.json()

    print(data)

    weather = data.get('weather', {})
    category = weather.get('category','UNKNOWN')

    forecast = data.get('forecast',{})

    temp = forecast.get('temp', 0.0)

    bring = category.lower().strip() in {'rain','mist'}

    umbrella = UmbrellaStatus(bring_umbrella = bring, temp = temp)


    #print(data)
    return umbrella
