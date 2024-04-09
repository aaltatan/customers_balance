import axios from "axios";

export const parseDate = (fullDate) => {
  let date = new Date(fullDate);
  let year = date.getFullYear();
  let month = (date.getMonth() + 1).toString().padStart(2, 0);
  let day = date.getDate().toString().padStart(2, 0);
  let hour = date.getHours().toString().padStart(2, 0);
  let minute = date.getMinutes().toString().padStart(2, 0);
  return `${year}-${month}-${day} ${hour}:${minute}`;
};

export function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export const getMessages = async () => {
  const response = await axios.get("/messages");
  try {
    const messages = response.data.trim();
    return messages;
  } catch (e) {
    console.log(e);
  }
};
