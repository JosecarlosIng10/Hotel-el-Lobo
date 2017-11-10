<%@ Page Title="" Language="C#" MasterPageFile="~/Principal.Master" AutoEventWireup="true" CodeBehind="Registrarse.aspx.cs" Inherits="ElLobo.Registrarse" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="contenidoContextual" runat="server">
</asp:Content>
<asp:Content ID="Content3" ContentPlaceHolderID="contenidoPrincipal" runat="server">
     <p>
        <h2>Nombre de Usuario&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="TextBox1" runat="server" Width="186px"></asp:TextBox>
    </h2>
    <h2>Contraseña&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:TextBox ID="TextBox2" runat="server" Width="179px"></asp:TextBox>
&nbsp; </h2>
     <h2>Direccion&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:TextBox ID="TextBox3" runat="server" Width="179px"></asp:TextBox>
&nbsp; </h2>
     <h2>Telefono&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:TextBox ID="TextBox4" runat="server" Width="179px"></asp:TextBox>
&nbsp; </h2>
     <h2>Edad&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:TextBox ID="TextBox5" runat="server" Width="179px"></asp:TextBox>
&nbsp; </h2>
     <p>     <asp:FileUpload id="FileUploadControl" runat="server" />
    <asp:Button ID="Button2" runat="server" Text="Cargar" Width="103px" Height="22px" OnClick="Button2_Click" />
    <br />
    <asp:TextBox ID="TextBox6" runat="server" Height="245px" Width="396px" TextMode="MultiLine"></asp:TextBox>
    <br />
     </p>
    <p style="margin-left: 200px">
        <asp:Button ID="Button1" runat="server" Text="Registrarse" Width="116px" OnClick="Button1_Click" />
    </p>
&nbsp;&nbsp;&nbsp; </asp:Content>
