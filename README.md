# Seals-and-Poetics-converter
Scrapes prices for items and shows the best things to spend GC seals and Tombstones of Poetics  on in FFXIV.

Currrently only works for Aether data center due to how the API works 
(if you want other data centers edit line 153 in the python script, Its part of 'def api_grab' and tells the script which data center to search)

Checks Universalis API against all sellable items that can be bought with either Tomstones of Poetics or Grand Company seals. 
Returns a top 15 list of the best value items to buy that are currently up on the API lists the website adress to copy/paste into browser.

Just because something is at the top of the list doesn't mean it will sell for that. Check the volume traded and history to make sure the item actually sells.
Ignored all Market restricted items and untradeables.
Removed the 'large ticket' house items. They are high priced, but low volume. Return will be high, but this program is more focused on quick flipping poetics and seals.
They constantly cloud the top 10, but not enough sell per day to justify buying tons


These price checks are snapshots of the market from the universalis api as it stands when the button is pressed. Universalis updates thier api every few hours.
These price checks do not take into account history or volume. Just the price on the api divided by the cost at the vendor. 
