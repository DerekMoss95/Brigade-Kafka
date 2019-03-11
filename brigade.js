const { events, Job } = require("brigadier");

events.on("exec", function(even, project) {
  console.log("beginning " + even.revision.commit)

  // Create a new job
  var job = new Job("generate-report", "python:3.6.8-slim-jessie")
  console.log(even.payload)
  console.log(even.buildID)
  console.log(even)
  job.env = {
    mySecretRef: even.payload
  }

  
  job.tasks = [
    "echo ${mySecretRef} > /src/brigade-scripts/mysecret",
    "cd /src/brigade-scripts",
    "pip3 install -r requirements.txt",
    "chmod +x generateReportUpdated.py",
    "python3 generateReportUpdated.py '${mySecretRef}'",
    ]
  console.log("set the tasks")


  // Display logs from the job Pod
  job.streamLogs = true;
  console.log("set logs to true")


  // We're done configuring, so we run the job
  job.run()
  console.log("run tests")

});

// events.on("push", function(e, project) {
//   console.log("beginning " + e.revision.commit)
//   console.log(project.secrets)
//   // Create a new job
//   var job = new Job("generate-report", "python:3.6.8-slim-jessie")
//   console.log("new job created")
//   //project.secrets.username
//   // Now we want it to run these commands in order:
//   // Ask how to access secrets in brigade.js file
//   job.env = {
//     mySecretReference: {
//       secretKeyRef: {
//         name: "mysecret",
//         key: "AppData"
//        }
//      }
//   };

//   job.tasks = [
//     "echo hello ${mySecretReference}",
//     "cd /src/brigade-scripts",
//     "ls -la",
//     "pip3 install -r requirements.txt",
//     "chmod +x generateReport.py",
//     "python3 generateReport.py",
// 	  "echo ${mySecretReference}"
//   ]
//   console.log("set the tasks")


//   // Display logs from the job Pod
//   job.streamLogs = true;
//   console.log("set logs to true")


//   // We're done configuring, so we run the job
//   job.run()
//   console.log("run tests")

// });

 
 
