#!/usr/bin/env bash

curl 'https://8psnffqtxq-dsn.algolia.net/1/indexes/Job_production/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.22.1)%3B%20Browser' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://climatebase.org' \
  -H 'Referer: https://climatebase.org/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'x-algolia-api-key: d2ebe27d3cc3d35fea04da7b1b0718a8' \
  -H 'x-algolia-application-id: 8PSNFFQTXQ' \
  --data-raw '{"query":"","page":"0","hitsPerPage":1000,"clickAnalytics":true,"filters":"","facets":["*","active","employer_has_approval","categories","sub_categories","job_types","sectors","drawdown_solutions","org_types","org_sizes","experience_levels","remote_preferences","employer_id"],"facetFilters":["active:true","employer_has_approval:true",["id:-29340874"],["id:-46605467"],["id:-47385433"],["id:-47385435"],["countries:United States"]],"enablePersonalization":false,"enableABTest":false}' > jobs_data.json
  