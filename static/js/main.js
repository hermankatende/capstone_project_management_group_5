// main.js for dashboard charts
// Requires Chart.js loaded from CDN in base.html

document.addEventListener('DOMContentLoaded', function() {
  // Only run if dashboard chart containers exist
  if (document.getElementById('dashboard-bar-chart')) {
    // Bar chart for entity counts
    new Chart(document.getElementById('dashboard-bar-chart'), {
      type: 'bar',
      data: {
        labels: ['Programs', 'Projects', 'Participants', 'Outcomes', 'Facilities', 'Equipment', 'Services'],
        datasets: [{
          label: 'Entity Counts',
          data: [
            parseInt(document.getElementById('count-programs').textContent),
            parseInt(document.getElementById('count-projects').textContent),
            parseInt(document.getElementById('count-participants').textContent),
            parseInt(document.getElementById('count-outcomes').textContent),
            parseInt(document.getElementById('count-facilities').textContent),
            parseInt(document.getElementById('count-equipment').textContent),
            parseInt(document.getElementById('count-services').textContent)
          ],
          backgroundColor: [
            '#d90429', '#222', '#fff200', '#d90429', '#222', '#fff200', '#d90429'
          ]
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          title: { display: true, text: 'System Entity Overview' }
        }
      }
    });
  }
});
