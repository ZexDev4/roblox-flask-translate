const express = require("express");
const fetch = require("node-fetch");

const app = express();
app.use(express.json());

app.post("/", async (req, res) => {
  try {
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

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Proxy failed" });
  }
});

module.exports = app;
