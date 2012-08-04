use warnings;
use strict;

use MediaWiki::API;

# http://seahttp://search.cpan.org/~dcollins/MediaWiki-Bot-2.3.1/lib/MediaWiki/Bot.pm

sub EditPage {
    my $mw=shift;
    my $pagename = shift;

    $mw->edit( {
	action => 'delete', title => $pagename, reason => 'Attack Pages' } )
	|| die $mw->{error}->{code} . ': ' . $mw->{error}->{details};
    
}

sub GetPages {
    my $mw = MediaWiki::API->new();
    $mw->{config}->{api_url} = 'http://speedydeletion.wikia.com/api.php';


my $username;
my $userpass;

open IN, "<config.cfg" or die;
while (<IN>)
{
    if (/username:(.+)/)
    {
	$username=$1;
    }
    elsif (/userpass:(.+)/)
    {
	$userpass=$1;
    }
}
close IN;
#print "User:$username Pass:$userpass\n";
die unless $username;
die unless $userpass;

$mw->login( { lgname => $username, lgpassword => $userpass } )
    || die $mw->{error}->{code} . ': ' . $mw->{error}->{details};
    


    foreach my $cat (
	"Category:Candidates_for_speedy_deletion_as_attack_pages",
	){
	# get a list of articles in category
	my $articles = $mw->list ( {
	    action => 'query',
	    list => 'categorymembers',
	    cmtitle => $cat,
	    cmlimit => 'max' } )
	    || die $mw->{error}->{code} . ': ' . $mw->{error}->{details};
	
	# and print the article titles
	foreach (@{$articles}) {
	    print "going to delete $_->{title}\n";
	    EditPage $mw, $_->{title};
	}
    }

}


GetPages;
