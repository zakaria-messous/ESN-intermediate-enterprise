// Sélectionnez tous les champs d'entrée du formulaire
let inputs = document.querySelectorAll('input, select, textarea');

// Écoutez les événements de saisie sur les champs d'entrée
inputs.forEach(input => {
  input.addEventListener('input', function() {
    // Vérifiez si le champ est valide
    if (input.checkValidity()) {
      // Ajoutez la classe is-valid et supprimez la classe is-invalid
      input.classList.add('is-valid');
      input.classList.remove('is-invalid');
    } else {
      // Ajoutez la classe is-invalid et supprimez la classe is-valid
      input.classList.add('is-invalid');
      input.classList.remove('is-valid');
    }
  });
});

// Écoutez l'événement de soumission du formulaire
document.querySelector('form').addEventListener('submit', function(event) {
  // Empêchez la soumission du formulaire si des champs sont invalides
  if (!this.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
  }

  // Ajoutez la classe was-validated pour activer les styles de validation Bootstrap
  this.classList.add('was-validated');
});
