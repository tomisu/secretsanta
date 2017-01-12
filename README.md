## Introduction
This project is a simple Django-based Secret Santa Manager.
* Create a Room
* Add participants
* Generate matches
* Share the URL
* Check and protect your match


## Technical description
The project consists in 2 separate django apps: "api", and "webapp".

The app "api", provides an API, so it can be used as a backend by the "webapp", or for example, by a bot developed later on.
The app "webapp" provides easy user interaction with the API.


## Product discussion
The most challenging thing about this project was thinking about user access.

I think that users seeking this kind of service don't want to register themselves, let alone register every participant. But they also don't want other people to be able to look at their giftee.

The solution I came up with is password-protected entries:
    When an entry (gifter->giftee) is access for the first time, a password is asked.
    To access the entry again, a password is needed. This way no one can sneak a peek, but you can refresh your memory.

The problem with this system is that people can check your giftee before you do, and lock it.


## How to improve it
I'd implement a report system in case someone checked your giftee before you.

Rooms could be protected by password if the user wants to.

Registration could be added, so users could have a list of their Secret Santas Rooms.
Registered users wouldn't need to use password to check the matches.
