import api from "./api";

export function logout() {
  return api.post("/api-auth/logout/");
}
