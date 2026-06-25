/* Evidence-Tier Funnel Visualization
 * D3.js funnel chart for evidence tier progression
 */

// Placeholder API endpoint for evidence tier data
const tierDataEndpoint = '/api/limen/evidence-tiers';

// Set up SVG container
const funnelSvg = d3.select('#evidence-funnel')
  .append('svg')
  .attr('width', 600)
  .attr('height', 400);

// Define funnel dimensions
const funnel = {
  width: 600,
  height: 400,
  minX: 50,
  maxX: 550,
  minY: 20,
  maxY: 380
};

// Fetch and visualize data
fetch(tierDataEndpoint)
  .then(response => response.json())
  .then(data => visualizeFunnel(data))
  .catch(error => console.error('Data fetch error:', error));

function visualizeFunnel(data) {
  // Example implementation using D3.funnel
  const funnelChart = d3.funnel()
    .x(d => d.x)
    .y(d => d.y)
    .radius(d => d.radius || 10)
    .value(d => d.value);

  // Create groups for each tier
  const tiers = funnelSvg.selectAll('.tier')
    .data(data)
    .enter()
    .append('g')
    .attr('class', 'tier')
    .attr('transform', d => `translate(${d.x}, ${d.y})`);

  // Draw funnel shapes
  tiers.append('path')
    .attr('d', funnelChart.path())
    .attr('fill', (d, i) => ['#4A90E2', '#69B200', '#ED1C24', '#FFC          '][i]);

  // Add value labels
  tiers.append('text')
    .attr('dx', '.35em')
    .attr('dy', '.35em')
    .text(d => `${d.stage}: ${d.count}`);
}
