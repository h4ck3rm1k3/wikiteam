use warnings;
use strict;

use MediaWiki::API;

# http://seahttp://search.cpan.org/~dcollins/MediaWiki-Bot-2.3.1/lib/MediaWiki/Bot.pm

 sub EditPage {
     my $mw=shift;
     my $pagename = shift;
     my $ok =$mw->edit( { action => 'delete', title => $pagename, reason => 'Attack Pages' } )	 ;

     if ($ok)	 {
	 warn "$pagename deleted\n";
     }  else     {
	 if (
	     ($mw->{error}->{code} != 5)
	     &&
	     ($mw->{error}->{code} != 3)
	     )
	 { #Page does not exist
	     warn $mw->{error}->{code} . ': ' . $mw->{error}->{details} ;
	 }
	 
     }

    
 }

sub GetPages {
    my $mw = MediaWiki::API->new();
    $mw->{config}->{api_url} = 'http://deletionpedia.dbatley.com/w/api.php';

    my $mw2 = MediaWiki::API->new();
    $mw2->{config}->{api_url} = 'http://speedydeletion.wikia.com/api.php';
    my $username;
    my $userpass;
    open IN, "<config.cfg" or die;
    while (<IN>)
    {
	if (/username:(.+)/)	{	    $username=$1;    }
	elsif (/userpass:(.+)/)    {	$userpass=$1;    }
    }
    close IN;
#print "User:$username Pass:$userpass\n";
    die unless $username;
    die unless $userpass;
    
    $mw2->login( { lgname => $username, lgpassword => $userpass } )
	|| die $mw2->{error}->{code} . ': ' . $mw2->{error}->{details};
    
 
    foreach my $cat (
	"Deletionpedia:Pages_blanked_after_complaints",
	"Deletionpedia:Blanked_pages",	
	"Deletionpedia:Dangerous_pages"
	){
	print "checking $cat\n";
	# get a list of articles in category
	my $articles = $mw->list ( {
	    action => 'query',
	    list => 'categorymembers',
#	    cmtitle => $cat,
cmcategory => $cat,
#	    cmlimit => 'max' 
	    cmlimit => '50', 


	  #http://deletionpedia.dbatley.com/w/api.php?format=json&action=query&cmcategory=Deletionpedia:Pages_blanked_after_complaints&cmlimit=50&list=categorymembers
				   } )
	    || die $mw->{error}->{code} . ': ' . $mw->{error}->{details};
	
	# and print the article titles
	foreach (@{$articles}) {
	    #print "going to delete $_->{title}\n";
	    EditPage $mw2, $_->{title};
	}
    }

}


GetPages;
