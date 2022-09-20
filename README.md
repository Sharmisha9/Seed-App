# 440-Group-24-Fall-2022
Repository for CS 440 Group 24 for Fall 2022

Note:  The presentation evaluation form and rubric are provided here for reference
       and planning purposes.  Hard copies will be handed out in class on 
       presentation days.  ( Unless presentations are given online, in which case
       a Google form will be made available. )
       
       Similarly the Group Project Member Evaluation Rubric is provided here for 
       reference only.  A form will be provided periodically during the term 
       for completion by all group members.


## Seed-app
to start app:
       npm start


## Clean File Structure Example  (will be deleted)
## Folder Structure example with Social App
### assets
 it is a collection of the (public) resource directories such as images, svg, company's logo,  etc..
       - This resource can be shared across the entire app.

### commons



### pages
it is a collection of directories that contains each page folder. 
       - sign-up, sign-in, main, settings, account-manager etc.. 
 * each page will have 
 directories:
       - components
              * sub component directories
              - comments
              - likes
              - etc.. 

       - hooks (hooks for the components)
              * sub directories
              - use-get-comments
              - use-get-likes
              - use-create-commnet
 files: 
       - models.js
       - style.css
       - utils.js


### setup
it is a collection of directories that needed for setting up the app.
       - context-manager (api manager), auth (for data authentification), routes-manager (manages multiple routes in the app). 


### store
it is a collection of directories for Python Redux, for example.
       - action
       - reducers
