const { events, Job } = require("brigadier");
events.on("exec", () => {
  var job = new Job("do-something", "alpine:3.8");
  job.tasks = [
    "wget -O data.json https://support.oneskyapp.com/hc/en-us/article_attachments/202761627/example_1.json",
    "head data.json"
  ];

  job.run();
});
