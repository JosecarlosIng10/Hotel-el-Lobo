<%@ Page Title="" Language="C#" MasterPageFile="~/Opciones.master" AutoEventWireup="true" CodeBehind="EliminarUsuario.aspx.cs" Inherits="ElLobo.EliminarUsuario" %>
<asp:Content ID="Content1" ContentPlaceHolderID="contenidoPrincipal" runat="server">
    <h1>Usuario:
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
    </h1>
    
    <p>&nbsp;</p>
    <p>
        <asp:Button ID="Button1" runat="server" Text="Eliminar" Width="120px" OnClick="Button1_Click" />
    </p>&nbsp;</p>
</asp:Content>
