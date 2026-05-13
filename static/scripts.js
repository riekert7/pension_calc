document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('projectionChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ages,
            datasets: [
                {
                    label: 'Projected Balance',
                    data: balances,
                    borderColor: '#1a1a2e',
                    backgroundColor: 'rgba(26, 26, 46, 0.08)',
                    fill: true,
                    tension: 0.3,
                    pointRadius: 2,
                },
                {
                    label: 'Total Contributed',
                    data: contributed,
                    borderColor: '#aaa',
                    borderDash: [5, 5],
                    fill: false,
                    tension: 0.3,
                    pointRadius: 2,
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'bottom' },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            return context.dataset.label + ': ' + symbol + context.parsed.y.toLocaleString();
                        }
                    }
                }
            },
            scales: {
                y: {
                    ticks: {
                        callback: function (value) {
                            return symbol + value.toLocaleString();
                        }
                    }
                },
                x: {
                    title: { display: true, text: 'Age' }
                }
            }
        }
    });
});