import { useState } from "react";
import api from "../services/api";
import { getCSRFToken } from "../services/csrf";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {

      const formData = new FormData();
      formData.append("username", username);
      formData.append("password", password);

      const csrfToken = getCSRFToken();

      await api.post("/api-auth/login/", formData, {
        headers: {
          "X-CSRFToken": csrfToken,
        },
      });

      // login OK
      window.location.href = "/reservas";
    } catch (err) {
      console.error(err);
      setError("Usuário ou senha inválidos");
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: "50px auto" }}>
      <h2>Login</h2>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Usuário</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>

        <div>
          <label>Senha</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>

        {error && <p style={{ color: "red" }}>{error}</p>}

        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}

export default Login;
