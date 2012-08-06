use warnings;
use strict;

use MediaWiki::API;

# http://seahttp://search.cpan.org/~dcollins/MediaWiki-Bot-2.3.1/lib/MediaWiki/Bot.pm

sub EditPage {
    my $mw=shift;
    my $pagename = shift;
    my $ref = $mw->get_page( { title => $pagename } );
    my $text=  $ref->{'*'};
    my $newtext = "{{copyvioblanked|$pagename}}\n";

    my $linktext;
    my $reftext;

    unless ( $ref->{missing} ) {
	my $timestamp = $ref->{timestamp};

	my $count =0;

	my $text2=$text;
	while ($text2 =~ s/\[\s*(http:[^\s\|\}\]]+)\]/DONE/g)	{ $linktext .= "* {{copyviolink|$1}}\n";	}
	# just grabe the raw http
	while ($text2 =~ s/(http:[^\s\|\}\]]+)\]/DONE/g)	{ $linktext .= "* {{copyviolink|$1}}\n";	}	
	while ($text2 =~ s/(https:[^\s\|\}\]]+)\]/DONE/g)	{ $linktext .= "* {{copyviolink|$1}}\n";	}	
	while ($text2 =~ s/\=(http:[^\s\|\}\]]+)\}/DONE/g)	{ $linktext .= "* {{copyviolink|$1}}\n";	}	

	if ($linktext){
	    $newtext .= "==External Links==\n$linktext";
	}

	while ($text =~ m/<ref>([^\<]+)<\/ref>/g)
	{
	    $reftext .= "*<ref>$1</ref>\n";
	}

	if ($reftext)
	{
	    $newtext .= "==References==\n$reftext";
	    $newtext .=	"\n<references/>\n";
	}

	#Creative CommonsAttribution-Share Alike 3.0 Unported license
	
	print "NewText : $newtext";

	if (1) {
	    $mw->edit( 
		{
		    action => 'edit',
		    title => $pagename,
		    basetimestamp => $timestamp, # to avoid edit conflicts
		    text => $newtext 
		}
		)
		|| die $mw->{error}->{code} . ': ' . $mw->{error}->{details};
	}
	
    }
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
	"Category:CopyVioNotMentioned",
	"Category:Possible_copyright_violations",
	"Category:Articles_tagged_for_copyright_problems", 
	"Category:Candidates_for_speedy_deletion_as_copyright_violations",
	"Category:All_copied_and_pasted_articles_and_sections",
      "Category:Candidates_for_speedy_deletion_by_user", # we dont want to keep what the author does not want.
#	"Category:Candidates_for_speedy_deletion_as_attack_pages"
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
	    print "$_->{title}\n";
	    EditPage $mw, $_->{title};
	}
    }

}


GetPages;
