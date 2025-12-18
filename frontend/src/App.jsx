import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from './components/Layout'
import Login from "./pages/Login";
import ReservasList from './pages/ReservasList'

function App() {
  return (
    <BrowserRouter>
      <Layout>
        <h2>Bem-vindo ao sistema</h2>
        <p>Interface em React conectada ao backend Django</p>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/reservas" element={<ReservasList />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}

export default App
