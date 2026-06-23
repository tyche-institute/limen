
# Parent Source Extraction Summary


Total reviewed rows: {len(tsv_results)}

Verdict distribution:
""
verdict_counts = {}
for result in tsv_results:
    verdict = result['bulk_source_verdict']
    verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
for verdict, count in verdict_counts.items():
    summary += f'- {verdict}: {count} ({count/len(tsv_results)*100:.1f}%)

summary += 