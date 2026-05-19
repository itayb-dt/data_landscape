# Backlog

## Interesting technologies 
https://github.com/rerun-io/rerun 

The data layer for physical AI
Log, query, visualize, and stream to training on shared columnar storage built for multimodal data.

What it does: Rerun ingests multi-rate, multimodal data (images, point clouds, transforms, time series, joint states, video) from many sources and formats (robot logs, human-data rigs, sim, web video; MCAP, rrd, LeRobot). The built-in viewer renders everything in sync, in realtime: scrub episodes, compare sensors side-by-side, watch CV pipelines run live. The same data is queryable with dataframes or SQL, and streams directly into training. Built in Rust on column-chunk storage purpose-built for multi-rate physical data. SDKs in Python, Rust, and C++.

Quickstart: pip install rerun-sdk — log your first multimodal data and see it in the viewer in under 2 minutes.

Run the Rerun Viewer in your browser
Read about what Rerun is and who it is for
Use cases
Ingest robot logs, egocentric/UMI rigs, sim, and web video into one substrate
Run CV pipelines (SLAM, hand tracking, motion retargeting) as table edits
Query raw, intermediate, and derived data with dataframes or SQL
Visualize multi-rate, multimodal sequences across the pipeline
Stream dataset mixes directly to training — no export jobs, no stale copies
Data types
Multi-rate, multimodal, spatial: images, point clouds, time series, tensors, transforms, joint states, video. Preserved end-to-end.

