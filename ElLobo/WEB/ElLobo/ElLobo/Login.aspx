<%@ Page Title="" Language="C#" MasterPageFile="~/Principal.Master" AutoEventWireup="true" CodeBehind="Login.aspx.cs" Inherits="ElLobo.Login" %>
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
<p style="margin-left: 200px">
    <asp:Button ID="Button1" runat="server" Text="Iniciar Sesion" Width="116px" OnClick="Button1_Click" />
</p>
&nbsp;&nbsp;&nbsp; </asp:Content>
