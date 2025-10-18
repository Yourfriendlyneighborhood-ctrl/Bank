document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const dashboard = document.getElementById('dashboard');
  const quickBalance = document.getElementById('quickBalance');

  loginForm.addEventListener('submit', (ev) => {
    ev.preventDefault();
    // THIS IS A DEMO: replace with real authentication calls.
    const user = loginForm.username.value.trim();
    if (!user) { alert('Enter username'); return; }
    // show dashboard preview
    dashboard.hidden = false;
    dashboard.querySelector('.account-overview .balance').textContent = '£1,234.56';
  });

  quickBalance.addEventListener('click', () => {
    // quick unsecured preview — in a real app use secure API + MFA
    alert('Quick balance: £1,234.56 (demo)');
  });

  document.getElementById('biometrics').addEventListener('click', () => {
    alert('Biometric sign-in placeholder (demo).');
  });
});
