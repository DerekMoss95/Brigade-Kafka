const { events, Job } = require("brigadier");

events.on("exec", function(e, project) {
  console.log("beginning " + e.revision.commit)

  // Create a new job
  var job = new Job("generate-report", "python:3.6.8-slim-jessie")
  console.log("new job created")

  // Now we want it to run these commands in order:
  job.tasks = [
    "cd /src/brigade-scripts",
    "ls -la",
    "pip install -r requirements.txt",
    "chmod +x generateReport.py",
    "python generateReport.py"
  ]
  console.log("set the tasks")


  // Display logs from the job Pod
  job.streamLogs = true;
  console.log("set logs to true")


  // We're done configuring, so we run the job
  job.run()
  console.log("run tests")

})
