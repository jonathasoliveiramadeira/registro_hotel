import { useEffect, useState } from "react";
import api from "../services/api";

function ReservasList() {
  const [reservas, setReservas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    api
      .get("http://localhost:8000/api/reservas/")
      .then((response) => {
        setReservas(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setErro("Erro ao buscar registros");
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Carregando...</p>;
  if (erro) return <p>{erro}</p>;

  return (
    <>
      <h2>Lista de Registros (teste)</h2>

      {reservas.length === 0 && <p>Nenhum registro encontrado.</p>}

      <ul>
        {reservas.map((r) => (
          <li key={r.id}>
            <strong>Reserva #{r.id}</strong><br />
            Cliente: {r.cliente_nome}<br />
            Quarto: {r.quarto}<br />
            Entrada: {r.data_entrada}<br />
            Saída: {r.data_saida}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ReservasList;
