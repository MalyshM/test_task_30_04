import {useState} from "react";
import axios from 'axios';
import './temperature.css';

const TemperaturePage = () => {
    // State variables to store the input values
    const [location, setLocation] = useState('');
    const [latitude, setLatitude] = useState('');
    const [longitude, setLongitude] = useState('');
    const [temperatureData, setTemperatureData] = useState([]);
    const href = 'http://localhost:8090/api/temperature_by_location'
    // Function to handle the button click event
    const handleLocationButtonClick = async () => {
        try {
            const response = await axios.get(href, {
                params: {name_str: location},
            });
            setTemperatureData(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const handleCoordinatesButtonClick = async () => {
        try {
            const response = await axios.get(href, {
                params: {long: parseFloat(longitude), lat: parseFloat(latitude)},
            });
            setTemperatureData(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Страница температуры</h1>
            <div>
                <label>Город:</label>
                <input type="text" value={location} onChange={(e) => setLocation(e.target.value)}/>
                <button onClick={handleLocationButtonClick}>Узнать прогноз погоды по городу</button>
            </div>
            <div>
                <label>Широта:</label>
                <input type="text" value={latitude} onChange={(e) => setLatitude(e.target.value)}/>
                <label>Долгота:</label>
                <input type="text" value={longitude} onChange={(e) => setLongitude(e.target.value)}/>
                <button onClick={handleCoordinatesButtonClick}>Узнать прогноз погоды по координатам</button>
            </div>
            <div>
                <h2>Прогноз погоды:</h2>
                <table className="temperature-table">
                    <thead>
                    <tr>
                        <th>Время</th>
                        <th>Давление воздуха на уровне моря</th>
                        <th>Температура воздуха</th>
                        <th>Облачность</th>
                        <th>Относительная влажность</th>
                        <th>Направление ветра</th>
                        <th>Скорость ветра</th>
                    </tr>
                    </thead>
                    <tbody>
                    {temperatureData.map((dataItem, index) => (
                        <tr key={index}>
                            <td>{dataItem.time}</td>
                            <td>{dataItem.data.instant.details.air_pressure_at_sea_level}</td>
                            <td>{dataItem.data.instant.details.air_temperature}°С</td>
                            <td>{dataItem.data.instant.details.cloud_area_fraction}%</td>
                            <td>{dataItem.data.instant.details.relative_humidity}%</td>
                            <td>{dataItem.data.instant.details.wind_from_direction}°</td>
                            <td>{dataItem.data.instant.details.wind_speed}м/с</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default TemperaturePage;