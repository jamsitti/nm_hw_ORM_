Task list left to do (last worked on Fri 3/12 8pm):

1. Pokemon model
  - how to instantiate it DONEDONE
  - connection to teams (many to many?) DONEDONE
  - how to add/remove to team (liking/disliking?)
  - find way to use API to connect pokemon_sprite??? like ooooof DONEDONE

2. UserTeam model
  - set up in html a way to create and view DONEDONE
  - make sure views create it DONEDONE
  - have some type of "-create==true" attribute or something, to use as a key to   make sure users can only make one team and that one team is tied to their profile
  - figure out how to set that you can only have six pokemon, and how to add pokemon
  to class... gorl
  -NEW: models wont let me import User model from accounts app, and therefore I can't link the foreignKey between UserTeams and Users. I am currently using this link to authenticate if a team has been made but because it's not working, when I load the 'teams' page it just asks if I want to make another (when I should only be able to have
  one per account)

3. User model:
  - make sure it connects to userTeam
  - just do a lil proofread and make sure everything is all cuteness

4. URLS:
  - check and see if you need to make anymore paths. You might need to make paths to the view functions such as liking, disliking, editing profiles/teams, etc

5. HOME:
  - make home display 3 random teams? Mean I need to populate like 6 lol
  - double check her sis

6. Search view:
  - she's the most functional but she needs some help... figure out what to do with that sprite call for sure, possibly add liking and disliking into the function

7. User page view:
  - need to set up a way in html to check if you can properly make userteam forms
  - need to set up a way to block userteam form if one is made. some type of boolean key?

8. Update team view:
  - theres some issues there gorl get it to work in the html then you can fix
  - figure out if you need to use the updateteamform, and if you dont, delete it

9. View teams view:
  - populate and test her out baybee

10. figure out wtf is going on with poke id

11. like and delete you already know you gotta deal with this stuff

12. Figure out what html pages you need to create and then... create them