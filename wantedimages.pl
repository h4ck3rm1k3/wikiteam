use LWP::Simple;
use Try::Tiny;

binmode STDOUT, ':utf8';
#$content = get("http://speedydeletion.wikia.com/wiki/Special:WantedFiles?limit=10000");

my $offset = shift @ARGV ||0;
$content = get("http://speedydeletion.wikia.com/wiki/Special:WantedFiles?limit=500&offset=${offset}");


use MediaWiki::API;

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


my $mw2 = MediaWiki::API->new();
$mw2->{config}->{api_url} = 'http://en.wikipedia.org/w/api.php';
#my $title=shift;
print $file;
use Encode;
use File::Copy;
#<li><s><a href="/wiki/File:

while ($content =~ m/\>File:([^<]+)</g)
{
    my $n=$1;
    print "looking at $n\n";

    next if ($n =~ /\//); # skip slashes in the name
    next if ($n =~ /\\/); # skip slashes in the name
    next if ($n =~ /http:/); # skip urls

    if (/<li><s><a href=\"\/wiki\/File:$n/)
    {
	print "Skip\n";
	next;
    }

    if (/(<li.+File:$n)/)
    {
	print "Skip $n\n";
	next;
    }

    my $f="images/$n";
    if ( -f $f) 
    {
	if ($f =~ /svg$/i)
	{
	    print "Skipping\n";
	}
	else
	{

	    $f =~ s/\s+/\ /g;
	    print "Uploading via python $f\n";
	    my $cmd = "python /home/mdupont/experiments/wikipedia/pywikipediabot/upload.py -noverify -keep -filename:\"$n\" \"$f\"";
	    print "$cmd\n";
	    my $ret = system "$cmd";
	    warn "ERROR:$ret" unless $ret ==0;
	}
	
	next;
    }

    print "check $n";
    my $file = $mw2->download( { title => "File:$n" } )
	|| warn "Cannot download $n " . $mw2->{error}->{code} . ': ' . $mw2->{error}->{details};
    
    if ($file ) 
    {
	print "$url\n";
	print $image;   
	print "got file \"$n\"\n";
	my $newcontent = encode('utf-8', $file); 
	
	open OUT,">tmp1_${f}";
#    binmode OUT, ':utf8';
#    print OUT $newcontent;
#    close OUT;
#    warn "created tmp1_${f}";
	############
	
	open OUT,">tmp_${f}";
	print OUT $file;
	close OUT;
	warn "created tmp_${f}";
	############
	
	# read it back in
	open IN,"tmp_${f}";
	binmode IN, ':utf8';
	#print IN $file;
	my $data="";
	while (<IN>) {
	    $data .= $_;
	}
	close IN;
	
	my $newcontent = encode('utf-8', $data); 
	
	print "check data " . length($newcontent);

	if ($f =~ /svg$/i)
	{
	    print "Skipping\n";
	    try {
		$mw->upload( { title => "$n",
			       summary => '{{wikipedia-image|$n}}',
			       data => $newcontent } ) || warn "Failed upload :" . $mw->{error}->{code} . ': ' . $mw->{error}->{details};
		
		move ("tmp_${f}","${f}");
	    }
	    catch   {
		warn "error! $_";
	    }

	}
	else
	{

	    $f =~ s/\s+/\ /g;
	    print "Uploading via python $f\n";
	    my $cmd = "python /home/mdupont/experiments/wikipedia/pywikipediabot/upload.py -noverify -keep -filename:\"$n\" \"tmp_$f\"";
	    print "$cmd\n";
	    my $ret = system "$cmd";
	    warn "Failed $ret" unless $ret ==0;
	    move ("tmp_${f}","${f}");
	}


    }
    else
    {
	warn "cannot download $f";
    }
    
    print "Done!\n";   
}



