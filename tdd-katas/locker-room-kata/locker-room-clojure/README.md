# Locker room kata

## Description

Imagine a wall with lockers in a locker room. All lockers are centrally opened and closed by a controller, where you can enter a PIN. When a locker is open, it is available and can be locked by entering a PIN. When a locker is closed, it can be opened with the PIN used to lock it. 

### Tentative TODO list

- [ ] a locker is unlocked initially
- [ ] a locker can be locked by entering a PIN for that locker
- [ ] a locker can be unlocked by entering the correct ping for that locker
- [ ] unlocking fails when pin is incorrect
- [ ] asking state or entering PIN for non-existing locker, fails
- [ ] PIN confirm on locking a locker
- [ ] A user can retry a pin on a locked locker
- [ ] unlocking fails after two retries
- [ ] the master key opens any locker