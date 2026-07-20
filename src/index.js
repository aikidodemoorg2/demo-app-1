import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/redirect", (req, res) => {
  res.redirect(`http://${req.hostname}:3000${req.url}`);
});

app.get("/error", (req, res) => {
  throw new Error("Something broke!");
});

app.get("/payments", (req, res) => {
  // Retrieve Stripe API key from environment variables, not hardcoded
  const STRIPE_API_KEY = process.env.STRIPE_API_KEY;
  
  // Never expose the API key in responses
  if (!STRIPE_API_KEY) {
    return res.status(500).json({ 
      error: "Payment service configuration error" 
    });
  }
  
  // Return safe payment configuration without exposing credentials
  res.status(200).json({ 
    status: "ready",
    provider: "stripe",
    // API key is available for internal use but never sent to client
    message: "Payment service is configured"
  });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send("Something broke!", err);
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
