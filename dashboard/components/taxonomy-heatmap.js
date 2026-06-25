/* Taxonomy Heatmap Visualization
 * D3.js heatmap for taxonomy categories
 */

// Placeholder API endpoint for taxonomy data
const taxonomyEndpoint = '/api/limen/taxonomy';

// Set up SVG container
const heatmapSvg = d3.select('#taxonomy-heatmap')
  .append('svg')
  .attr('width', 800)
  .attr('height', 500);

// Fetch and visualize data
fetch(taxonomyEndpoint)
  .then(response => response.json())
  .then(data => visualizeHeatmap(data))
  .catch(error => console.error('Data fetch error:', error));

function visualizeHeatmap(data) {
  // Create a grid layout
  const rows = [...Array(10).keys()]; // Example 10x10 grid
  const cols = [...Array(20).keys()];

  // Compute cell dimensions
  const cellWidth = heatmapSvg.attr('width') / cols.length;
  const cellHeight = heatmapSvg.attr('height') / rows.length;

  // Create cells
  const cells = heatmapSvg.selectAll('.cell')
    .data(data)
    .enter()
    .append('rect')
    .attr('class', 'cell')
    .attr('x', (d, i) => (i % cols.length) * cellWidth)
    .attr('y', (d, i) => Math.floor(i / cols.length) * cellHeight)
    .attr('width', cellWidth)
    .attr('height', cellHeight)
    .attr('fill', (d, i) => {
      // Example: color based on index
      const colors = d3.scaleOrdinal(d3.schemeCategory10);
      return colors(i % 10);
    });
}
