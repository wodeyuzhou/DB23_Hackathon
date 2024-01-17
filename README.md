# DB23 Hackathon-bike-sharing-demand
https://www.kaggle.com/competitions/db23-hackathon/overview

![스크린샷 2024-01-17 16 01 44](https://github.com/wodeyuzhou/DB23_Hackathon/assets/104478598/a6822368-3421-4383-bc62-15745388e055)
- code/
    - main.py - Gradient Boost & Random Forest 사용, Private 1위 (RMSE, 55.63506)
    - main.ipynb - main.py 추가설명

### Data Fields
- dteday : date
- season : season (1:winter, 2:spring, 3:summer, 4:fall)
- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
- weekday : day of the week
- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
- weathersit :
    >1: Clear, Few clouds, Partly cloudy, Partly cloudy<br/> 
    >2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist<br/>
    >3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds<br/>
    >4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp : Normalized temperature in Celsius. 
    >The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
- atemp: Normalized feeling temperature in Celsius. 
    >The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
- hum: Normalized humidity. The values are divided to 100 (max)
- windspeed: Normalized wind speed. The values are divided to 67 (max)
- cnt: count of total rental bikes including both casual and registered

### 출처
- https://github.com/logicalguess/kaggle-bike-sharing-demand
- https://github.com/qinhanmin2014/kaggle-bike-sharing-demand