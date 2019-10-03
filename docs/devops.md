## DevOps

- What do you know about DevOps?

Your answer must be simple and straightforward. Begin by explaining the growing importance of DevOps in the IT industry. Discuss how such an approach aims to synergize the efforts of the development and operations teams to accelerate the delivery of software products, with a minimal failure rate. 

Include how DevOps is a value-added practice, where development and operations engineers join hands throughout the product or service lifecycle, right from the design stage to the point of deployment.

- Why has DevOps gained prominence over the last few years?
Before talking about the growing popularity of DevOps, discuss the current industry scenario. Begin with some examples of how big players such as Netflix and Facebook are investing in DevOps to automate and accelerate application deployment and how this has helped them grow their business. 

Using Facebook as an example, you would point to Facebook’s continuous deployment and code ownership models and how these have helped it scale up but ensure the quality of experience at the same time. Hundreds of lines of code are implemented without affecting quality, stability, and security.

Your next use case should be Netflix. This streaming and on-demand video company follow similar practices with fully automated processes and systems. Mention the user base of these two organizations: Facebook has 2 billion users while Netflix streams online content to more than 100 millions users worldwide.  

These are great examples of how DevOps can help organizations to ensure higher success rates for releases, reduce the lead time between bug fixes, streamline and continuous delivery through automation, and an overall reduction in manpower costs.

- Which are some of the most popular DevOps tools? Do you have experience working with any of these tools?
The more popular DevOps tools include:

1. Selenium
2. Puppet
3. Chef
4. Git
5. Jenkins
6. Ansible
7. Docker

Thoroughly describe any tools that you are confident about, what it’s abilities are and why you prefer using it. For example, if you have expertise in Git, you would tell the interviewer that Git is a distributed Version Control System (VCS) tool that allows the user to track file changes and revert to specific changes when required. Discuss how Git’s distributed architecture gives it an added edge where developers make changes locally and can have the entire project history on their local Git repositories, which can be later shared with other team members.

Now that you have mentioned VCS, be ready for the next obvious question.

- What is version control and why should VCS be used?

Define version control and talk about how this system records any changes made to one or more files and saves them in a centralized repository. VCS tools will help you recall previous versions and perform the following:

- Go through the changes made over a period of time and check what works versus what doesn’t.
- Revert specific files or specific projects back to an older version.
- Examine issues or errors that have occurred due to a particular change

Using VCS gives developers the flexibility to simultaneously work on a particular file and all modifications can be logically combined later.

- Is there a difference between Agile and DevOps? If yes, please explain.

As a DevOps engineer, interview questions like this are quite expected. Start by describing the obvious overlap between DevOps and Agile. Although the implementation of DevOps is always in sync with Agile methodologies, there is a clear difference between the two. The principles of Agile are associated with seamless production or development of a piece of software. On the other hand, DevOps deals with the development, followed by deployment of the software, ensuring faster turnaround time, minimum errors, and reliability

2. Why are configuration management processes and tools important?

Talk about multiple software builds, releases, revisions, and versions for each software or testware that is being developed. Move on to explain the need for storing and maintaining data, keeping track of development builds and simplified troubleshooting. Don’t forget to mention the key CM tools that can be used to achieve these objectives. Talk about how tools like Puppet, Ansible, and Chef help in automating software deployment and configuration on several servers.

3. How is Chef used as a CM tool?

The chef is considered to be one of the preferred industry-wide CM tools. Facebook migrated its infrastructure and backend IT to the Chef platform, for example. Explain how Chef helps you to avoid delays by automating processes. The scripts are written in Ruby. It can integrate with cloud-based platforms and configure new systems. It provides many libraries for infrastructure development that can later be deployed within a software. Thanks to its centralized management system, one Chef server is enough to be used as the center for deploying various policies.

4. How would you explain the concept of “Infrastructure as Code”(IaC)?

It is a good idea to talk about IaC as a concept, which is sometimes referred to as a programmable infrastructure, where infrastructure is perceived in the same way as any other code. Describe how the traditional approach to managing infrastructure is taking a back seat and how manual configurations, obsolete tools, and custom scripts are becoming less reliable. Next, accentuate the benefits of IaC and how changes to IT infrastructure can be implemented in a faster, safer and easier manner using IaC. Include the other benefits of IaC like applying regular unit testing and integration testing to infrastructure configurations, and maintaining up-to-date infrastructure documentation.

If you have completed a certification on Amazon Web Services (AWS), and are interviewing for niche roles such as AWS-certified DevOps engineer, here are some AWS DevOps interview questions that you must be prepared for:

5. What is the role of AWS in DevOps?

When asked this question in an interview, get straight to the point by explaining that AWS is a cloud-based service provided by Amazon that ensures scalability through unlimited computing power and storage. AWS empowers IT enterprises to develop and deliver sophisticated products and deploy applications on the cloud. Some of its key services include Amazon CloudFront, Amazon SimpleDB, Amazon Relational Database Service, and Amazon Elastic Computer Cloud. Discuss the various cloud platforms and emphasize any big data projects that you have handled in the past using cloud infrastructure.

6. How is IaC implemented using AWS?

Start by talking about the age-old mechanisms of writing commands onto script files and testing them in a separate environment before deployment and how this approach is being replaced by IaC. Similar to the codes written for other services, with the help of AWS, IaC allows developers to write, test, and maintain infrastructure entities in a descriptive manner, using formats such as JSON or YAML. This enables easier development and faster deployment of infrastructure changes.

As a DevOps engineer, an in-depth knowledge of processes, tools, and relevant technology are essential. You must also have a holistic understanding of the products, services, and systems in place. If your answers matched the answers we’ve provided above, you’re in great shape for future DevOps interviews. Good luck! If you’re looking for answers to specific DevOps interview questions that aren’t addressed here, ask them in the comments below. Our DevOps experts will help you craft the perfect answer.

7. Which are the top DevOps tools? Which tools have you worked on?

The most popular DevOps tools are mentioned below:
Git : Version Control System tool
Jenkins : Continuous Integration tool
Selenium : Continuous Testing tool
Puppet, Chef, Ansible : Configuration Management and Deployment tools
Nagios : Continuous Monitoring tool
Docker : Containerization tool

8. How do all these tools work together?

Given below is a generic logical flow where everything gets automated for seamless delivery. However, this flow may vary from organization to organization as per the requirement.

- Developers develop the code and this source code is managed by Version Control System tools like Git etc.
- Developers send this code to the Git repository and any changes made in the code is committed to this Repository.
- Jenkins pulls this code from the repository using the Git plugin and build it using tools like Ant or Maven.
- Configuration management tools like puppet deploys & provisions testing environment and then Jenkins releases this code on the test environment on which testing is done using tools like selenium.
- Once the code is tested, Jenkins send it for deployment on the production server (even production server is provisioned & maintained by tools like puppet).
- After deployment It is continuously monitored by tools like Nagios.
- Docker containers provides testing environment to test the build features.

9. What are the advantages of DevOps?

For this answer, you can use your past experience and explain how DevOps helped you in your previous job. If you don’t have any such experience, then you can mention the below advantages.

Technical benefits:

Continuous software delivery
Less complex problems to fix
Faster resolution of problems
Business benefits:

Faster delivery of features
More stable operating environments
More time available to add value (rather than fix/maintain)

10. What is the most important thing DevOps helps us achieve?

According to me, the most important thing that DevOps helps us achieve is to get the changes into production as quickly as possible while minimizing risks in software quality assurance and compliance. This is the primary objective of DevOps. Learn more in this DevOps tutorial blog.
However, you can add many other positive effects of DevOps. For example, clearer communication and better working relationships between teams i.e. both the Ops team and Dev team collaborate together to deliver good quality software which in turn leads to higher customer satisfaction.

11. Explain with a use case where DevOps can be used in industry/ real-life.

12. Explain your understanding and expertise on both the software development side and the technical operations side of an organization you have worked with in the past.

For this answer, share your past experience and try to explain how flexible you were in your previous job. You can refer the below example:
DevOps engineers almost always work in a 24/7 business-critical online environment. I was adaptable to on-call duties and was available to take up real-time, live-system responsibility. I successfully automated processes to support continuous software deployments. I have experience with public/private clouds, tools like Chef or Puppet, scripting and automation with tools like Python and PHP, and a background in Agile.


## Version Control System (VCS)

1. What is Version control?

This is probably the easiest question you will face in the interview. My suggestion is to first give a definition of Version control. It is a system that records changes to a file or set of files over time so that you can recall specific versions later. Version control systems consist of a central shared repository where teammates can commit changes to a file or set of file. Then you can mention the uses of version control.

Version control allows you to:
- Revert files back to a previous state.
- Revert the entire project back to a previous state.
- Compare changes over time.
- See who last modified something that might be causing a problem.
- Who introduced an issue and when.

2. What are the benefits of using version control?

I will suggest you to include the following advantages of version control:
- With Version Control System (VCS), all the team members are allowed to work freely on any file at any time. 
- VCS will later allow you to merge all the changes into a common version.
- All the past versions and variants are neatly packed up inside the VCS. When you need it, you can request any version at any time and you’ll have a snapshot of the complete project right at hand.
- Every time you save a new version of your project, your VCS requires you to provide a short description of what was changed. Additionally, you can see what exactly was changed in the file’s content. This allows you to know who has made what change in the project.
- A distributed VCS like Git allows all the team members to have complete history of the project so if there is a breakdown in the central server you can use any of your teammate’s local Git repository.

3. Describe branching strategies you have used.

This question is asked to test your branching experience so tell them about how you have used branching in your previous job and what purpose does it serves, you can refer the below points:

- Feature branching
A feature branch model keeps all of the changes for a particular feature inside of a branch. When the feature is fully tested and validated by automated tests, the branch is then merged into master.

- Task branching
In this model each task is implemented on its own branch with the task key included in the branch name. It is easy to see which code implements which task, just look for the task key in the branch name.

- Release branching
Once the develop branch has acquired enough features for a release, you can clone that branch to form a Release branch. Creating this branch starts the next release cycle, so no new features can be added after this point, only bug fixes, documentation generation, and other release-oriented tasks should go in this branch. Once it is ready to ship, the release gets merged into master and tagged with a version number. In addition, it should be merged back into develop branch, which may have progressed since the release was initiated.
In the end tell them that branching strategies varies from one organization to another, so I know basic branching operations like delete, merge, checking out a branch etc.

4. What is Git?

I will suggest that you attempt this question by first explaining about the architecture of git as shown in the below diagram. You can refer to the explanation given below:

- Git is a Distributed Version Control system (DVCS). It can track changes to a file and allows you to revert back to any particular change.
- Its distributed architecture provides many advantages over other Version Control Systems (VCS) like SVN one major advantage is that it does not rely on a central server to store all the versions of a project’s files. Instead, every developer “clones” a copy of a repository I have shown in the diagram below with “Local repository” and has the full history of the project on his hard drive so that when there is a server outage, all you need for recovery is one of your teammate’s local Git repository.
- There is a central cloud repository as well where developers can commit changes and share it with other teammates as you can see in the diagram where all collaborators are commiting changes “Remote repository”.

5. Explain some basic Git commands?

Below are some basic Git commands:

| Command | Function |
| ----------- | -------- |
| git config --global user.name "name" | configure author name to be used with your commits |
| git config --global user.email "email" | configure author email to be used with your commits | 
| git init | create new local repository |
| git clone path/to/repo | create working copy of local repo | 
| git clone username@host:/path/to/repo | for a remote server use | 
| git add <filname> | add one file |
| git add * | add more file |
| git commit -m "message" | commit canges to head |
| git push origin master | send changes to the master branch of your remote repo|
| git status | list the files u have changed and those u still need to add in commit |
| git remote add origin <server> | if u havent conencted |

- Culture
- Automation
- Measurement
- Sharing

- People over process over tools
- continuous delivery
- Lean management
- visible ops change control
- infrastructure as code

10 practises for devops success
- Incident command system
- developers on call
- public status pages
- blameless post mortem
- embedded teams
- the cloud
- andon cords
- dependency injection
- blue/green deployment
- chaos monkey

tool criteai 
- programmable
- verifible
- well behaved
- 

Teams:
developers
sysadmins
dba
noc
soc


- unit testing
- code quality/hygine
- integration test
- TDD 
- BDD beahviour 
- acceptance test driven ADTD
- Perforamce testing
- security testing

# CI Toolchain

1. Version Control(Github, SVN)
2. CI systems(Jenkins, travisci, circlrci)
3. Build(make/rake, maven, gulp, packer)
4. Test(Unit testing Junit, pytest| Integration test robot )
5. Artifact Repository(Artifactory, Nexus, Docker hub, AWS s3)
6. Deployment(Rundeck, deploynator)

# CD Toolchain

[Ansible](ansible.md)

## Continuous Integration

1. What is meant by Continuous Integration?

It is a development practice that requires developers to integrate code into a shared repository several times a day. Each check-in is then verified by an automated build, allowing teams to detect problems early.
I suggest that you explain how you have implemented it in your previous job. You can refer the below given example:

1. Developers check out code into their private workspaces.
2. When they are done with it they commit the changes to the shared repository (Version Control Repository).
3. The CI server monitors the repository and checks out changes when they occur.
4. The CI server then pulls these changes and builds the system and also runs unit and integration tests.
5. The CI server will now inform the team of the successful build.
6. If the build or tests fails, the CI server will alert the team.
7. The team will try to fix the issue at the earliest opportunity.
8. This process keeps on repeating.

2. Why do you need a Continuous Integration of Dev & Testing?

For this answer, you should focus on the need of Continuous Integration. My suggestion would be to mention the below explanation in your answer:
Continuous Integration of Dev and Testing improves the quality of software, and reduces the time taken to deliver it, by replacing the traditional practice of testing after completing all development. It allows Dev team to easily detect and locate problems early because developers need to integrate code into a shared repository several times a day (more frequently). Each check-in is then automatically tested.

3. What are the success factors for Continuous Integration?

Here you have to mention the requirements for Continuous Integration. You could include the following points in your answer:

- Maintain a code repository
- Automate the build
- Make the build self-testing
- Everyone commits to the baseline every day
- Every commit (to baseline) should be built
- Keep the build fast
- Test in a clone of the production environment
- Make it easy to get the latest deliverables
- Everyone can see the results of the latest build
- Automate deployment