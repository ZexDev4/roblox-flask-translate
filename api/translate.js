// contoh Node.js proxy
import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());

app.post("/translate", async (req, res) => {
  const { q, target } = req.body;
  const response = await fetch("https://webapi.laratranslate.com/translate/segmented", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-lara-client": "Webapp",
      "Origin": "https://app.laratranslate.com"
    },
    body: JSON.stringify({
      q,
      source: "",
      target,
      instructions: [],
      style: "faithful",
      adapt_to: [],
      glossaries: [],
      content_type: "text/plain"
    })
  });
  const data = await response.json();
  res.json(data);
});

app.listen(3000, () => console.log("Proxy running on port 3000"));
