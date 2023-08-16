use strict;
use warnings;

print "Please enter the time\n";
chomp (my $time = <STDIN>);

print "Do you have Monday Off?\n";
chomp (my $mondayOff = <STDIN>);

print "Do you have any Major Task?\n";
chomp (my $majorTask = <STDIN>);

print "Do you want to watch The Game Of Thrones?\n";
chomp (my $gameOfThrones = <STDIN>);

if ( ($time > 1000 || ($majorTask eq "No") == 0) && ($gameOfThrones eq "Yes") == 0 && ($mondayOff eq "Yes") == 0) {
    print "You can watch The Game Of Thrones\n";
} else {
    print "Sorry Buddy, you can't watch anything because you have work Monday & chores to do\n";  
}

