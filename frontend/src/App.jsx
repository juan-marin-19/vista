import { useEffect, useState } from "react";
import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000/api";

export default function App() {
  const [stations, setStations] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchStations = async () => {
      try {
        const response = await axios.get(`${API_BASE}/stations/`);
        setStations(response.data);
      } catch (err) {
        setError("No se pudieron cargar las estaciones.");
      }
    };
    fetchStations();
  }, []);

  return (
    <div className="page">
      <header className="hero">
        <h1>VRISA</h1>
        <p>Vigilancia de Riesgos e Inmisiones de Sustancias Atmosféricas</p>
      </header>
      <section className="card">
        <h2>Estaciones activas</h2>
        {error && <p className="error">{error}</p>}
        <ul>
          {stations.map((station) => (
            <li key={station.id}>
              <strong>{station.name}</strong>
              <span>{station.station_type}</span>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}
