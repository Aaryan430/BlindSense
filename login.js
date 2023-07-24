let text = "hello I want peace";

  // Create a new SpeechSynthesisUtterance object
  let utterance = new SpeechSynthesisUtterance();

  // Set the text and voice of the utterance
  utterance.text = text;
  utterance.voice = window.speechSynthesis.getVoices()[0];

  // Speak the utterance
  window.speechSynthesis.speak(utterance);